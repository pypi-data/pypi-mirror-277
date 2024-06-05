# Copyright 2023 The Chromium Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

import argparse
import dataclasses
import enum
import logging
import re
from typing import TYPE_CHECKING, Any, Dict, List, Optional, cast

from immutabledict import immutabledict

from crossbench import cli_helper, compat, plt
from crossbench.config import ConfigObject, ConfigParser
from crossbench.plt import ChromeOsSshPlatform

if TYPE_CHECKING:
  from crossbench.path import RemotePath, LocalPath


@enum.unique
class BrowserDriverType(compat.StrEnumWithHelp):
  WEB_DRIVER = ("WebDriver", "Use Selenium with webdriver, for local runs.")
  APPLE_SCRIPT = ("AppleScript", "Use AppleScript, for local macOS runs only")
  ANDROID = ("Android",
             "Use Webdriver for android. Allows to specify additional settings")
  IOS = ("iOS", "Placeholder, unsupported at the moment")
  LINUX_SSH = ("Remote Linux",
               "Use remote webdriver and execute commands via SSH")
  CHROMEOS_SSH = ("Remote ChromeOS",
                  "Use remote ChromeDriver and execute commands via SSH")

  @classmethod
  def default(cls) -> BrowserDriverType:
    return cls.WEB_DRIVER

  @classmethod
  def parse(cls, value: str) -> BrowserDriverType:
    identifier = value.lower()
    if identifier == "":
      return BrowserDriverType.default()
    if identifier in ("", "selenium", "webdriver"):
      return BrowserDriverType.WEB_DRIVER
    if identifier in ("applescript", "osa"):
      return BrowserDriverType.APPLE_SCRIPT
    if identifier in ("android", "adb"):
      return BrowserDriverType.ANDROID
    if identifier in ("iphone", "ios"):
      return BrowserDriverType.IOS
    if identifier == "ssh":
      return BrowserDriverType.LINUX_SSH
    if identifier == "chromeos-ssh":
      return BrowserDriverType.CHROMEOS_SSH
    raise argparse.ArgumentTypeError(f"Unknown driver type: {value}")

  @property
  def is_remote(self):
    if self.name in ("ANDROID", "CHROMEOS_SSH", "LINUX_SSH"):
      return True
    return False

  @property
  def is_local(self):
    return not self.is_remote


class AmbiguousDriverIdentifier(argparse.ArgumentTypeError):
  pass


IOS_UUID_RE = re.compile(r"[0-9A-Z]+-[0-9A-Z-]+")


@dataclasses.dataclass(frozen=True)
class DriverConfig(ConfigObject):
  type: BrowserDriverType = BrowserDriverType.default()
  path: Optional[RemotePath] = None
  device_id: Optional[str] = None
  settings: Optional[immutabledict] = None

  def __post_init__(self):
    if not self.type:
      raise ValueError(f"{type(self).__name__}.type cannot be None.")
    try:
      hash(self.settings)
    except ValueError as e:
      raise ValueError(
          f"settings must be hashable but got: {self.settings}") from e
    self.validate()

  @property
  def is_remote(self) -> bool:
    return self.type.is_remote

  @property
  def is_local(self) -> bool:
    return self.type.is_local

  def validate(self) -> None:
    if self.type == BrowserDriverType.ANDROID:
      self.validate_android()
    if self.type == BrowserDriverType.IOS:
      self.validate_ios()
    if self.type == BrowserDriverType.CHROMEOS_SSH:
      # Unlike the validation functions above for iOS and Android,
      # which validate the "host" to which the device is connected,
      # the ChromeOS validation function validates the "client".
      # Consider moving this logic elsewhere in the future.
      self.validate_chromeos()

  def validate_android(self) -> None:
    devices = plt.adb_devices(plt.PLATFORM)
    names = list(devices.keys())
    if not devices:
      raise argparse.ArgumentTypeError("No ADB devices attached.")
    if not self.device_id:
      if len(devices) == 1:
        # Default device "adb" (no settings) with exactly one device is ok.
        return
      raise AmbiguousDriverIdentifier(
          f"{len(devices)} ADB devices connected: {names}. "
          "Please explicitly specify a device ID.")
    if self.device_id not in devices:
      raise argparse.ArgumentTypeError(
          f"Could not find ADB device with device_id={repr(self.device_id)}. "
          f"Choices are {names}.")

  def validate_chromeos(self) -> None:
    platform = self.get_platform()
    assert isinstance(platform, plt.ChromeOsSshPlatform), \
           f"Invalid platform: {platform}"
    platform = cast(plt.ChromeOsSshPlatform, platform)
    if not platform.exists(platform.AUTOLOGIN_PATH):
      raise ValueError(f"Could not find `autotest` on {platform.host}."
                       "Please ensure that it is running a test image:"
                       "go/arc-setup-dev-mode-dut#usb-cros-test-image")

  def validate_ios(self) -> None:
    devices: Dict[str, Any] = plt.ios_devices(plt.PLATFORM)
    if not devices:
      raise argparse.ArgumentTypeError("No iOS devices attached.")
    names = list(map(str, devices))
    if not self.device_id:
      if len(devices) == 1:
        # Default device "ios" (no settings) with exactly one device is ok.
        return
      raise AmbiguousDriverIdentifier(
          f"{len(devices)} ios devices connected: {names}. "
          "Please explicitly specify a device UUID.")
    if self.device_id not in devices:
      raise argparse.ArgumentTypeError(
          f"Could not find ios device with device_id={repr(self.device_id)}. "
          f"Choices are {names}.")

  @classmethod
  def default(cls) -> DriverConfig:
    return cls(BrowserDriverType.default())

  @classmethod
  def loads(cls, value: str) -> DriverConfig:
    if not value:
      raise argparse.ArgumentTypeError("Cannot parse empty string")
    # Variant 1: $PATH
    path: Optional[LocalPath] = cli_helper.try_resolve_existing_path(value)
    driver_type: BrowserDriverType = BrowserDriverType.default()
    if not path:
      if cls.value_has_path_prefix(value):
        raise argparse.ArgumentTypeError(
            f"Driver path does not exist: {repr(value)}")
      # Variant 2: $DRIVER_TYPE
      if "{" != value[0]:
        try:
          driver_type = BrowserDriverType.parse(value)
        except argparse.ArgumentTypeError as original_error:
          try:
            return cls.load_short_settings(value, plt.PLATFORM)
          except AmbiguousDriverIdentifier:  # pylint: disable=try-except-raise
            raise
          except ValueError as e:
            logging.debug("Parsing short inline driver config failed: %s", e)
            raise original_error from e
      else:
        # Variant 2: full hjson config
        data = cli_helper.parse_inline_hjson(value)
        return cls.load_dict(data)
    if path and path.stat().st_size == 0:
      raise argparse.ArgumentTypeError(f"Driver path is empty file: {path}")
    return DriverConfig(driver_type, path)

  @classmethod
  def load_short_settings(cls, value: str,
                          platform: plt.Platform) -> DriverConfig:
    """Check for short versions and multiple candidates"""
    logging.debug("Looking for driver candidates: %s", value)
    candidate: Optional[DriverConfig]
    if candidate := cls.try_load_adb_settings(value, platform):
      return candidate
    if platform.is_macos:
      if candidate := cls.try_load_ios_settings(value, platform):
        return candidate
    # TODO: add more custom parsing here
    raise ValueError("Unknown setting")

  @classmethod
  def try_load_adb_settings(cls, value: str,
                            platform: plt.Platform) -> Optional[DriverConfig]:
    candidate_serials: List[str] = []
    pattern: re.Pattern = cls.compile_search_pattern(value)
    for serial, info in plt.adb_devices(platform).items():
      if pattern.fullmatch(serial):
        candidate_serials.append(serial)
        continue
      for key, info_value in info.items():
        if (pattern.fullmatch(f"{key}:{info_value}") or
            pattern.fullmatch(info_value)):
          candidate_serials.append(serial)
          break
    if len(candidate_serials) > 1:
      raise AmbiguousDriverIdentifier(
          "Found more than one adb devices matching "
          f"'{value}': {candidate_serials}")
    if len(candidate_serials) == 0:
      logging.debug("No matching adb devices found.")
      return None
    assert len(candidate_serials) == 1
    return DriverConfig(
        BrowserDriverType.ANDROID, device_id=candidate_serials[0])

  @classmethod
  def try_load_ios_settings(cls, value: str,
                            platform: plt.Platform) -> Optional[DriverConfig]:
    candidate_serials: List[str] = []
    pattern: re.Pattern = cls.compile_search_pattern(value)
    for uuid, device_info in plt.ios_devices(platform).items():
      if pattern.fullmatch(uuid):
        candidate_serials.append(uuid)
        continue
      if pattern.fullmatch(device_info.name):
        candidate_serials.append(uuid)
        continue
    if len(candidate_serials) > 1:
      raise AmbiguousDriverIdentifier(
          "Found more than one ios devices matching "
          f"'{value}': {candidate_serials}")
    if len(candidate_serials) == 0:
      logging.debug("No matching ios devices found.")
      return None
    assert len(candidate_serials) == 1
    return DriverConfig(BrowserDriverType.IOS, device_id=candidate_serials[0])

  @classmethod
  def compile_search_pattern(cls, maybe_pattern: str) -> re.Pattern:
    try:
      return re.compile(maybe_pattern)
    except Exception as e:
      logging.debug(
          "Falling back to full string match for "
          "invalid regexp search pattern: %s %s", maybe_pattern, e)
      return re.compile(re.escape(maybe_pattern))

  @classmethod
  def load_dict(cls, config: Dict[str, Any]) -> DriverConfig:
    return cls.config_parser().parse(config)

  @classmethod
  def config_parser(cls) -> ConfigParser[DriverConfig]:
    parser = ConfigParser("DriverConfig parser", cls)
    parser.add_argument(
        "type",
        type=BrowserDriverType.parse,
        default=BrowserDriverType.default())
    parser.add_argument(
        "settings",
        type=immutabledict,
        help="Additional driver-dependent settings.")
    parser.add_argument(
        "device_id",
        type=driver_device_id,
        depends_on=("settings",),
        help="Device ID / Serial ID / Unique device name")
    return parser

  def get_ssh_platform(self) -> plt.Platform:
    assert self.settings
    host = cli_helper.parse_non_empty_str(self.settings.get("host"), "host")
    port = cli_helper.parse_port(self.settings.get("port"), "port")
    ssh_port = cli_helper.parse_port(self.settings.get("ssh_port"), "ssh port")
    ssh_user = cli_helper.parse_non_empty_str(
        self.settings.get("ssh_user"), "ssh user")
    if self.type == BrowserDriverType.CHROMEOS_SSH:
      return plt.ChromeOsSshPlatform(
          plt.PLATFORM,
          host=host,
          port=port,
          ssh_port=ssh_port,
          ssh_user=ssh_user)
    return plt.LinuxSshPlatform(
        plt.PLATFORM,
        host=host,
        port=port,
        ssh_port=ssh_port,
        ssh_user=ssh_user)

  def get_platform(self) -> plt.Platform:
    if self.type == BrowserDriverType.ANDROID:
      return plt.AndroidAdbPlatform(plt.PLATFORM, self.device_id)
    if self.type == BrowserDriverType.IOS:
      # TODO(cbruni): use `xcrun xctrace list devices` to find the UDID
      # for attached simulators or devices. Currently only a single device
      # is supported
      pass
    if (self.type == BrowserDriverType.LINUX_SSH or
        self.type == BrowserDriverType.CHROMEOS_SSH):
      return self.get_ssh_platform()
    return plt.PLATFORM


def driver_device_id(device_id: Optional[str],
                     settings: Optional[immutabledict]) -> Optional[str]:
  if not settings:
    return device_id
  settings_device_id = settings.get("device_id")
  if not device_id:
    return settings_device_id
  if settings_device_id != device_id:
    raise TypeError("Conflicting both driver['settings']['device_id'] "
                    "and driver['device_id']: "
                    f"{repr(settings_device_id)} vs {repr(device_id)}")
  return device_id
