l1 = list(input("Введите элементы через пробел - ").split())
# print(l1)
# print(n)
if len(l1) % 2 == 0:
    l1.index()
    i = 0
    for i in range(int(len(l1))):
        l1[i: i+1:]
        # l1[::2], l1[1::2] = l1[1::2], l1[::2]
    print(f'кол-во элементов четное {l1}')
else:
    l1[::2], l1[1::2], = l1[1::2], l1[::2]
    print(f'кол-во элементов нечетное {l1}')



#print(l1.reverse()) почему так не срабатывает? результат выводит None

