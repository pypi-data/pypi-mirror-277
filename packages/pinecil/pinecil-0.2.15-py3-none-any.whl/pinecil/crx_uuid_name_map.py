bulk_data_names_v220 = {
    "00000001-0000-1000-8000-00805f9b34fb": "BulkData",
    "00000002-0000-1000-8000-00805f9b34fb": "Accelerometer",
    "00000003-0000-1000-8000-00805f9b34fb": "Build",
    "00000004-0000-1000-8000-00805f9b34fb": "DeviceID",
}

bulk_data_names_v221beta2 = {
    "9eae1001-9d0d-48c5-aa55-33e27f9bc533": "BulkData",
    "9eae1002-9d0d-48c5-aa55-33e27f9bc533": "Accelerometer",
    "9eae1003-9d0d-48c5-aa55-33e27f9bc533": "Build",
    "9eae1004-9d0d-48c5-aa55-33e27f9bc533": "DeviceID",
}

names_v220 = {
    "00000000-0000-1000-8000-00805f9b34fb": "save_to_flash",
    "00000001-0000-1000-8000-00805f9b34fb": "SetTemperature",
    "00000002-0000-1000-8000-00805f9b34fb": "SleepTemperature",
    "00000003-0000-1000-8000-00805f9b34fb": "SleepTimeout",
    "00000004-0000-1000-8000-00805f9b34fb": "DCInCutoff",
    "00000005-0000-1000-8000-00805f9b34fb": "MinVolCell",
    "00000006-0000-1000-8000-00805f9b34fb": "QCMaxVoltage",
    "00000007-0000-1000-8000-00805f9b34fb": "DisplayRotation",
    "00000008-0000-1000-8000-00805f9b34fb": "MotionSensitivity",
    "00000009-0000-1000-8000-00805f9b34fb": "AnimLoop",
    "0000000a-0000-1000-8000-00805f9b34fb": "AnimSpeed",
    "0000000b-0000-1000-8000-00805f9b34fb": "AutoStart",
    "0000000c-0000-1000-8000-00805f9b34fb": "ShutdownTimeout",
    "0000000d-0000-1000-8000-00805f9b34fb": "CooldownBlink",
    "0000000e-0000-1000-8000-00805f9b34fb": "AdvancedIdle",
    "0000000f-0000-1000-8000-00805f9b34fb": "AdvancedSoldering",
    "00000010-0000-1000-8000-00805f9b34fb": "TemperatureUnit",
    "00000011-0000-1000-8000-00805f9b34fb": "ScrollingSpeed",
    "00000012-0000-1000-8000-00805f9b34fb": "LockingMode",
    "00000013-0000-1000-8000-00805f9b34fb": "PowerPulsePower",
    "00000014-0000-1000-8000-00805f9b34fb": "PowerPulseWait",
    "00000015-0000-1000-8000-00805f9b34fb": "PowerPulseDuration",
    "00000016-0000-1000-8000-00805f9b34fb": "VoltageCalibration",
    "00000017-0000-1000-8000-00805f9b34fb": "BoostTemperature",
    "00000018-0000-1000-8000-00805f9b34fb": "CalibrationOffset",
    "00000019-0000-1000-8000-00805f9b34fb": "PowerLimit",
    "0000001a-0000-1000-8000-00805f9b34fb": "ReverseButtonTempChange",
    "0000001b-0000-1000-8000-00805f9b34fb": "TempChangeLongStep",
    "0000001c-0000-1000-8000-00805f9b34fb": "TempChangeShortStep",
    "0000001d-0000-1000-8000-00805f9b34fb": "HallEffectSensitivity",
    "0000001e-0000-1000-8000-00805f9b34fb": "AccelMissingWarningCounter",
    "0000001f-0000-1000-8000-00805f9b34fb": "PDMissingWarningCounter",
    "00000020-0000-1000-8000-00805f9b34fb": "UILanguage",
    "00000021-0000-1000-8000-00805f9b34fb": "PDNegTimeout",
    "00000022-0000-1000-8000-00805f9b34fb": "ColourInversion",
    "00000023-0000-1000-8000-00805f9b34fb": "Brightness",
    "00000024-0000-1000-8000-00805f9b34fb": "LOGOTime",
    "00000025-0000-1000-8000-00805f9b34fb": "CalibrateCJC",
}


def reduce_idx(idx: str) -> str:
    parts = idx.split("-")
    first_group_as_number = int(parts[0], 16)
    # '& 0xffff' makes int unsigned (ensures -1 becomes 0x0000ffff):
    new_first_group_as_hex = f"{first_group_as_number-1 & 0xffff:08x}"
    return "-".join([new_first_group_as_hex] + parts[1:])


names_v221beta1 = {
    **{reduce_idx(k): v for k, v in names_v220.items()},
    "00000025-0000-1000-8000-00805f9b34fb": "BLEEnabled",
    "0000fffe-0000-1000-8000-00805f9b34fb": "SettingsReset",
}

names_v221beta2 = {
    "f6d70000-5a10-4eba-aa55-33e27f9bc533": "SetTemperature",
    "f6d70001-5a10-4eba-aa55-33e27f9bc533": "SleepTemperature",
    "f6d70002-5a10-4eba-aa55-33e27f9bc533": "SleepTimeout",
    "f6d70003-5a10-4eba-aa55-33e27f9bc533": "DCInCutoff",
    "f6d70004-5a10-4eba-aa55-33e27f9bc533": "MinVolCell",
    "f6d70005-5a10-4eba-aa55-33e27f9bc533": "QCMaxVoltage",
    "f6d70006-5a10-4eba-aa55-33e27f9bc533": "DisplayRotation",
    "f6d70007-5a10-4eba-aa55-33e27f9bc533": "MotionSensitivity",
    "f6d70008-5a10-4eba-aa55-33e27f9bc533": "AnimLoop",
    "f6d70009-5a10-4eba-aa55-33e27f9bc533": "AnimSpeed",
    "f6d7000a-5a10-4eba-aa55-33e27f9bc533": "AutoStart",
    "f6d7000b-5a10-4eba-aa55-33e27f9bc533": "ShutdownTimeout",
    "f6d7000c-5a10-4eba-aa55-33e27f9bc533": "CooldownBlink",
    "f6d7000d-5a10-4eba-aa55-33e27f9bc533": "AdvancedIdle",
    "f6d7000e-5a10-4eba-aa55-33e27f9bc533": "AdvancedSoldering",
    "f6d7000f-5a10-4eba-aa55-33e27f9bc533": "TemperatureUnit",
    "f6d70010-5a10-4eba-aa55-33e27f9bc533": "ScrollingSpeed",
    "f6d70011-5a10-4eba-aa55-33e27f9bc533": "LockingMode",
    "f6d70012-5a10-4eba-aa55-33e27f9bc533": "PowerPulsePower",
    "f6d70013-5a10-4eba-aa55-33e27f9bc533": "PowerPulseWait",
    "f6d70014-5a10-4eba-aa55-33e27f9bc533": "PowerPulseDuration",
    "f6d70015-5a10-4eba-aa55-33e27f9bc533": "VoltageCalibration",
    "f6d70016-5a10-4eba-aa55-33e27f9bc533": "BoostTemperature",
    "f6d70017-5a10-4eba-aa55-33e27f9bc533": "CalibrationOffset",
    "f6d70018-5a10-4eba-aa55-33e27f9bc533": "PowerLimit",
    "f6d70019-5a10-4eba-aa55-33e27f9bc533": "ReverseButtonTempChange",
    "f6d7001a-5a10-4eba-aa55-33e27f9bc533": "TempChangeLongStep",
    "f6d7001b-5a10-4eba-aa55-33e27f9bc533": "TempChangeShortStep",
    "f6d7001c-5a10-4eba-aa55-33e27f9bc533": "HallEffectSensitivity",
    "f6d7001d-5a10-4eba-aa55-33e27f9bc533": "AccelMissingWarningCounter",
    "f6d7001e-5a10-4eba-aa55-33e27f9bc533": "PDMissingWarningCounter",
    "f6d7001f-5a10-4eba-aa55-33e27f9bc533": "UILanguage",
    "f6d70020-5a10-4eba-aa55-33e27f9bc533": "PDNegTimeout",
    "f6d70021-5a10-4eba-aa55-33e27f9bc533": "ColourInversion",
    "f6d70022-5a10-4eba-aa55-33e27f9bc533": "Brightness",
    "f6d70023-5a10-4eba-aa55-33e27f9bc533": "LOGOTime",
    "f6d70024-5a10-4eba-aa55-33e27f9bc533": "CalibrateCJC",
    "f6d70025-5a10-4eba-aa55-33e27f9bc533": "BLEEnabled",
    "f6d70026-5a10-4eba-aa55-33e27f9bc533": "PDVpdoEnabled",
    "f6d7ffff-5a10-4eba-aa55-33e27f9bc533": "save_to_flash",
    "f6d7fffe-5a10-4eba-aa55-33e27f9bc533": "SettingsReset",
}
