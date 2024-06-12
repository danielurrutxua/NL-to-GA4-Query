import random
from .constants.filter_type_enum import FilterType
from .constants.equal_variants import variants as equal_variants
from .constants.filter_object_enum import FilterObject
from .constants.countries import countries
def generate():
    match random.choice(list(FilterType)):
        case FilterType.EQUALS: return equals()
        case FilterType.MORE_THAN: return equals()
        case FilterType.LESS_THAN: return equals()

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
            return "pais", "country", country["Spanish"], country["English"]
        case FilterObject.ACTIVE_USERS:
            num = random.randint(1, 100000)
            return "usuarios activos", "activeUsers", str(num), str(num) 
        case FilterObject.DEVICE_CATEGORY:
            device_category = random.choice(("desktop", "tablet", "phone"))
            return "tipo de dispositivo", "deviceCategory", device_category, device_category