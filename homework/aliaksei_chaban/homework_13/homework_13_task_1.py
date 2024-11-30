import os
import datetime


homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
mentors_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(mentors_file_path) as mentors_file:
        for line in mentors_file.readlines():
            yield date_extractor(line)


def date_extractor(line):
    x = line.split(' - ')[0][3:]
    return x


def date_to_python(dict_with_dates, date_key):
    return datetime.datetime.strptime(dict_with_dates.get(date_key), '%Y-%m-%d %H:%M:%S.%f')


def add_seven_days(date_to_extend):
    return date_to_extend + datetime.timedelta(days=7)


def week_day(date_to_search):
    return date_to_search.strftime('%A')


def how_long_passed(date_in_past):
    return datetime.datetime.now() - date_in_past


date_dict = {}
counter = 1

for date in read_file():
    date_dict[counter] = date
    counter += 1

line = int(input("Дату из какой линии вы хотите преобразовать? Выберите 1-3 "))

if line == 1:
    first_line = date_to_python(date_dict, line)
    print('-' * 150)
    print(f'Дата из первой строки увеличена на 7 дней: {add_seven_days(first_line)}')
elif line == 2:
    second_line = date_to_python(date_dict, line)
    print('-' * 150)
    print(f'Дата во второй строке это - {week_day(second_line)}')
elif line == 3:
    third_line = date_to_python(date_dict, line)
    print('-' * 150)
    print(f'С момента даты в третье строке прошло: {how_long_passed(third_line)}')
else:
    print('В доступе только 3 строки')
