import random
from ..query_generators.utils.resources import get_random_dimension
from .constants.data_type_enum import DataType
from .constants.filter_type_enum import FilterType
from .constants.equal_variants import variants as equal_variants
from .constants.filter_object_enum import FilterObject
from .constants.countries import countries
from .constants.device_categories import device_categories, device_category_synonyms
from .constants.browsers import browsers, browser_synonyms
from .constants.cities import cities
from .constants.sources import sources, source_synonyms


def generate():
    dimension = get_random_dimension()

    match DataType.valueOf(dimension.iloc[3]):
        case DataType.STRING:
            


def equals():
    variant = random.choice(equal_variants)
    object_sp, object_en, value_sp, value_en = choose_object_value()
    phrase = variant.format(object=object_sp, value=value_sp)
    api_query = f"{object_en} == {value_en}"
    return phrase, api_query


def choose_object_value():
    match random.choice(list(FilterObject)):
        case FilterObject.COUNTRY:
            country = random.choice(countries)
            return "pais", "country", country[1], country[0]
        case FilterObject.ACTIVE_USERS:
            num = random.randint(1, 100000)
            return "usuarios activos", "activeUsers", str(num), str(num)
        case FilterObject.DEVICE_CATEGORY:
            device_category = random.choice(device_categories)
            return (
                random.choice(device_category_synonyms),
                "deviceCategory",
                random.choice(device_categories[0]),
                device_category[1],
            )
        case FilterObject.BROWSER:
            browser = random.choice(browsers)
            return (
                random.choice(browser_synonyms),
                "browser",
                random.choice(browser[1]),
                browser[0],
            )
        case FilterObject.CITY:
            city = random.choice(cities)
            return "ciudad", "city", city[1], city[0]
        case FilterObject.SOURCE:
            source = random.choice(sources)
            return (
                random.choice(source_synoyms),
                "source",
                random.choice(source[0]),
                source[1],
            )
