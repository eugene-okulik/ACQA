# Даны числа x и y. Получить x − y / 1 + xy


def formula_result(x, y):
    return x - y / 1 + x * y


x_value = 5
y_value = 3

print(formula_result(x_value, y_value))