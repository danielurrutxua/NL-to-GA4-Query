import random
from .constants.date_range_enum import DateRange
from .types.year import generate as year
from .types.year_range import generate as year_range
from .types.month import generate as month
from .types.month_range import generate as month_range
from .types.day import generate as day
from .types.day_range import generate as day_range
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
        case DateRange.TODAY: return today()
        case DateRange.YESTERDAY: return yesterday()
        case DateRange.DAYS_AGO: return days_ago()
        case DateRange.WEEKS_AGO: return weeks_ago()
        case DateRange.MONTHS_AGO: return months_ago()
        case DateRange.YEARS_AGO: return years_ago()    

            