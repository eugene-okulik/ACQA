import random


def is_increase(employee_salary):
    bonus = random.choice([True, False])
    if bonus:
        new_salary = employee_salary + random.randrange(100, 501)
    else:
        new_salary = employee_salary
    print(f'{employee_salary}, {bonus} - "${new_salary}"')


salary = int(input('Введи вашу зарплату: '))
is_increase(salary)
