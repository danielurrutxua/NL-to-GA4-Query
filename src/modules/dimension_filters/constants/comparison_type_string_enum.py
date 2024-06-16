from enum import Enum


class ComparisonTypeString(Enum):
    EXACT = 0
    BEGINS_WITH = 1
    ENDS_WITH = 2
    CONTAINS = 3
