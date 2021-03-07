str1 = input('Введите строку - ').split()

for i, word in enumerate(str1, 10):
    if len(word) <= 10:
        print(word)
    else:
        print(word[:10])


# на проверку