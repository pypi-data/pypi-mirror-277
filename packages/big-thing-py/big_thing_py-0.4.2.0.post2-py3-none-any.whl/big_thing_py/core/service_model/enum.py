from aenum import IntEnum, StrEnum


class MXStrEnum(StrEnum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class MXIntEnum(IntEnum):
    def _generate_next_value_(name, start, count, last_values):
        return count
