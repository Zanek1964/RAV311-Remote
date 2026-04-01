from __future__ import annotations
from dataclasses import dataclass

PIONEER_FREQUENCY_HZ = 40_000

_HEADER_HIGH_US = 9000
_HEADER_LOW_US = 4500
_BIT_HIGH_US = 560
_ONE_LOW_US = 1690
_ZERO_LOW_US = 560
_TRAILER_HIGH_US = 560
_TRAILER_LOW_US = 25500


@dataclass
class Timing:
    high_us: int
    low_us: int


def _encode_uint16_lsb(value: int) -> list[Timing]:
    """Encode 16 bits LSB first, exactement comme NEC/Pioneer ESPHome."""
    result = []
    for _ in range(16):
        if value & 1:
            result.append(Timing(_BIT_HIGH_US, _ONE_LOW_US))
        else:
            result.append(Timing(_BIT_HIGH_US, _ZERO_LOW_US))
        value >>= 1
    return result


def _encode_frame(rc_code: int) -> list[Timing]:
    """
    Suit exactement pioneer_protocol.cpp d'ESPHome :
    address = (rc_code & 0xff00) | (~(rc_code >> 8) & 0xff)
    command = bits 0-3 de rc_code inversés en position → octet haut,
              octet bas = complément de l'octet haut
    """
    address = (rc_code & 0xFF00) | ((~(rc_code >> 8)) & 0xFF)

    cmd_high = 0
    for bit in range(4):
        if (rc_code >> bit) & 1:
            cmd_high |= (1 << (7 - bit))
    command = (cmd_high << 8) | ((~cmd_high) & 0xFF)

    timings: list[Timing] = [Timing(_HEADER_HIGH_US, _HEADER_LOW_US)]
    timings.extend(_encode_uint16_lsb(address))
    timings.extend(_encode_uint16_lsb(command))
    timings.append(Timing(_TRAILER_HIGH_US, _TRAILER_LOW_US))
    return timings


@dataclass
class PioneerCommand:
    rc_code: int
    repeat: int = 2

    @property
    def modulation(self) -> int:
        return PIONEER_FREQUENCY_HZ

    def get_raw_timings(self) -> list[Timing]:
        frame = _encode_frame(self.rc_code)
        timings = list(frame)
        for _ in range(self.repeat - 1):
            timings.extend(frame)
        return timings
