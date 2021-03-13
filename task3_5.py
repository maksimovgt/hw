def sum_str():
    summa = 0
    while True:
        my_list = input('Введите числа через пробел или q для выхода: ').split()
        for n in my_list:
            if n == 'q':
                return summa
            else:
                try:
                    summa += int(n)
                except ValueError:
                    print('Нажмите q чтобы выйти')

        print(f'Сумма чисел в строке = {summa}')

sum_str()

#на проверку