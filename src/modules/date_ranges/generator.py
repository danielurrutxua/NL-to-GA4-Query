import random
from .constants.date_range_enum import DateRange
from .types.year import generate as year
from .types.year_range import generate as year_range
from .types.month import generate as month
from .types.month_range import generate as month_range
from .types.day import generate as day
from .types.day_range import generate as day_range
from .types.last_calendar_week import generate as last_calendar_week
from .types.last_calendar_month import generate as last_calendar_month
from .types.last_calendar_quarter import generate as last_calendar_quarter
from .types.last_calendar_year import generate as last_calendar_year
from .types.last_7_days import generate as last_7_days
from .types.last_14_days import generate as last_14_days
from .types.last_30_days import generate as last_30_days
from .types.last_90_days import generate as last_90_days
from .types.today import generate as today
from .types.yesterday import generate as yesterday
from .types.days_ago import generate as days_ago
from .types.weeks_ago import generate as weeks_ago
from .types.months_ago import generate as months_ago
from .types.years_ago import generate as years_ago

def generate():
    match random.choice(list(DateRange)):
        case DateRange.YEAR: return year()
        case DateRange.YEAR_RANGE: return year_range()
        case DateRange.MONTH: return month()
        case DateRange.MONTH_RANGE: return month_range()
        case DateRange.DAY: return day()
        case DateRange.DAY_RANGE: return day_range()
        case DateRange.LAST_CALENDAR_WEEK: return last_calendar_week()
        case DateRange.LAST_CALENDAR_MONTH: return last_calendar_month()
        case DateRange.LAST_CALENDAR_QUARTER: return last_calendar_quarter()
        case DateRange.LAST_CALENDAR_YEAR: return last_calendar_year()
        case DateRange.LAST_7_DAYS: return last_7_days()
        case DateRange.LAST_14_DAYS: return last_14_days()
        case DateRange.LAST_30_DAYS: return last_30_days()
        case DateRange.LAST_90_DAYS: return last_90_days()
        case DateRange.TODAY: return today()
        case DateRange.YESTERDAY: return yesterday()
        case DateRange.DAYS_AGO: return days_ago()
        case DateRange.WEEKS_AGO: return weeks_ago()
        case DateRange.MONTHS_AGO: return months_ago()
        case DateRange.YEARS_AGO: return years_ago()    

            