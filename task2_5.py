my_list = [9, 7, 7, 8, 6, 5, 4, 3, 2, 2, 2, 1]
r = int(input('Введите рейтинг - '))
i = 0
for n in my_list:
    if r <= n:
        i += 1
my_list.insert(i, r)
print(my_list)

#на проверку