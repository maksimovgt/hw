def int_func(word):
    word: str
    return word.title()


words = input('Введите слова через пробел - ').split()
for i in words:
    w = int_func(i)
    print(int_func(w))
