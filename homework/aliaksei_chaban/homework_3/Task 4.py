# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь


def hypotenuse_calculation(a, b):
    return (a ** 2 + b ** 2) ** 0.5


def triangle_area_calculation(a, b):
    return a * b * 0.5


first_side = 13
second_side = 8

print(hypotenuse_calculation(first_side, second_side))
print(triangle_area_calculation(first_side, second_side))
