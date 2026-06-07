import math


def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area


print(square(3.6))
print(square(8))
print(square(3.1))
