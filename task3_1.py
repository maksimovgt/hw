def divison(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return print('Ошибка, введите число')
    if b == 0:
        print('На ноль делить нельзя')
    else:
        return a / b

print(divison(input('Введите 1-ю переменную: '), input('Введите 2-ю переменую: ')))