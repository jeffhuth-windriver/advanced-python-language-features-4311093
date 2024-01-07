# Example file for Advanced Python: Language Features by Joe Marini
# define enumerations using the Enum base class
from enum import Enum, unique, auto

# TODO: enums have human-readable values and types
@unique # ensures values are not re-used
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOTMATO = 4
    PEAR = auto() # assigns 5

# TODO: enums have name and value properties
print(Fruit.APPLE)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))
print(Fruit.APPLE.name, Fruit.APPLE.value)

# TODO: print the auto-generated value
print(Fruit.PEAR.name, Fruit.PEAR.value)

# TODO: enums are hashable - can be used as keys
my_fruits = {}
my_fruits[Fruit.BANANA] = "Come Mr. Tally Man"
print(my_fruits)
print(my_fruits[Fruit.BANANA])
