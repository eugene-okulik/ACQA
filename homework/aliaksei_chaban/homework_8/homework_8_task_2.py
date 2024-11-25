import sys


def fibonacci_generator(limit=10000000000000000000):
    f1, f2 = 0, 1
    count_f = 0
    while count_f < limit:
        yield f1
        f1, f2 = f2, f1 + f2
        count_f += 1


sys.set_int_max_str_digits(10**6)
count = 0

for num in fibonacci_generator():
    if count == 5:
        print(num)
    elif count == 200:
        print(num)
    elif count == 1000:
        print(num)
    elif count == 100000:
        print(num)
        break
    count +=1
