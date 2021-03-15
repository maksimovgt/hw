from functools import reduce


def mult_func(a, b):
    return a * b


my_list = [el for el in range(100, 1001, 2)]

print([reduce(mult_func, my_list)])
#на проверку