from random import randint
with open('file5.txt', mode='w+', encoding='utf-8') as file:
    file.write(' '.join([str(randint(1, 10)) for el in range(100)]))
    file.seek(0)
    print(sum(map(int, file.readline().split())))



