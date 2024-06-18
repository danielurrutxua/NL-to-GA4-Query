from enum import Enum

class DateRange(Enum):
    YEAR = 1
    YEAR_RANGE = 2
    MONTH = 3
    MONTH_RANGE = 4
    DAY = 5
    DAY_RANGE = 6
    TODAY = 7
    YESTERDAY = 8
    DAYS_AGO = 9
    WEEKS_AGO = 10
    MONTHS_AGO = 11
    YEARS_AGO = 12