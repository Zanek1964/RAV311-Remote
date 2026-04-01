from __future__ import annotations
from homeassistant.components.infrared import RAWInfraredCommand
from homeassistant.components.infrared import Timing

PIONEER_FREQUENCY_HZ = 40_000
_HEADER_HIGH = 9000
_HEADER_LOW = 4500
_BIT_HIGH = 560
_ONE_LOW = 1690
_ZERO_LOW = 560
_TRAILER_HIGH = 560
_TRAILER_LOW = 25500


def _encode_uint16_lsb(value: int) -> list[Timing]:
    result = []
    for _ in range(16):
        if value & 1:
            result.append(Timing(high_us=_BIT_HIGH, low_us=_ONE_LOW))
        else:
            result.append(Timing(high_us=_BIT_HIGH, low_us=_ZERO_LOW))
        value >>= 1
    return result


def make_pioneer_command(rc_code: int, repeat: int = 2) -> RAWInfraredCommand:
    address = (rc_code & 0xFF00) | ((~(rc_code >> 8)) & 0xFF)
    cmd_high = 0
    for bit in range(4):
        if (rc_code >> bit) & 1:
            cmd_high |= (1 << (7 - bit))
    command = (cmd_high << 8) | ((~cmd_high) & 0xFF)

    frame: list[Timing] = [Timing(high_us=_HEADER_HIGH, low_us=_HEADER_LOW)]
    frame.extend(_encode_uint16_lsb(address))
    frame.extend(_encode_uint16_lsb(command))
    frame.append(Timing(high_us=_TRAILER_HIGH, low_us=_TRAILER_LOW))

    return RAWInfraredCommand(timings=frame, repeat_count=repeat - 1)
