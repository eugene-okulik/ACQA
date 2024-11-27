temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

high_temperatures = list(filter(lambda temp: temp > 28, temperatures))
max_temp = max(high_temperatures)
min_temp = min(high_temperatures)
average_temp = round(sum(high_temperatures) / len(high_temperatures))

print(f'Максимальная температура - {max_temp}')
print(f'Минимальная температура - {min_temp}')
print(f'Средняя температура - {average_temp}')
