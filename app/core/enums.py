from enum import Enum

class UserRole(str, Enum):
    user = "user"
    admin = "admin"
    customer = "customer"
    driver = "driver"
    restaurant = "restaurant"


class CuisineStyle(str, Enum):
    american = "american"
    chinese = "chinese"
    italian = "italian"
    japanese = "japanese"
    korean = "korean"
    mexican = "mexican"
    indian = "indian"
    thai = "thai"
    vietnamese = "vietnamese"
    french = "french"
    mediterranean = "mediterranean"
    other = "other"

class VehicleType(str, Enum):
    car = "car"
    motorcycle = 'motorcycle'