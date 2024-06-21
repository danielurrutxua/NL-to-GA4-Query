from enum import Enum


class MatchTypeInteger(Enum):
    EQUALS = 0
    GREATER_THAN = 1
    LESS_THAN = 2
    GREATER_THAN_OR_EQUAL = 3
    LESS_THAN_OR_EQUAL = 4
