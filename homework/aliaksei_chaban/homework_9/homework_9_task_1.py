import datetime

time = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(time, '%b %d, %Y - %X')
print(f'Полное название месяца - {python_date.strftime("%B")}')

my_formate_date = python_date.strftime('%d.%m.%Y, %H:%M')
print(f'Новый формат даты - {my_formate_date}')
