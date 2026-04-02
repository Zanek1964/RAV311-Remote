from __future__ import annotations
from dataclasses import dataclass, field
from infrared_protocols import Command, Timing

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


@dataclass
class PioneerCommand(Command):
    """Pioneer IR command compatible with infrared_protocols.Command."""

    rc_code: int
    repeat: int = 2
    modulation: int = field(default=PIONEER_FREQUENCY_HZ, init=False)

    def get_raw_timings(self) -> list[Timing]:
        address = (self.rc_code & 0xFF00) | ((~(self.rc_code >> 8)) & 0xFF)
        cmd_high = 0
        for bit in range(4):
            if (self.rc_code >> bit) & 1:
                cmd_high |= (1 << (7 - bit))
        command = (cmd_high << 8) | ((~cmd_high) & 0xFF)

        frame: list[Timing] = [Timing(high_us=_HEADER_HIGH, low_us=_HEADER_LOW)]
        frame.extend(_encode_uint16_lsb(address))
        frame.extend(_encode_uint16_lsb(command))
        frame.append(Timing(high_us=_TRAILER_HIGH, low_us=_TRAILER_LOW))

        timings = list(frame)
        for _ in range(self.repeat - 1):
            timings.extend(frame)
        return timings
