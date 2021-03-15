from itertools import count,cycle

for i in count(int(input('Введите число, для выхода введите q '))):
    print(i, end = '')
    quit = input()
    if quit == 'q':
        break

my_list = input('Введите символы через пробел, для выхода введите q! - ').split()
i = cycle(my_list)
quit = None
while quit != 'q':
    print(next(i), end='')
    quit = input()
#на проверку