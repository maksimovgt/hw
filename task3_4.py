def my_func(x, y):
    y: int
    x: int
    if x < 0 or y > 0:
        return print('Ошибка, не выполнены условия')
    else:
        return print(x ** y)


my_func(9, -2)

#на проверку