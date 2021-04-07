from random import randint
with open('file5.txt', mode='w+', encoding='utf-8') as file:
    file.write(" ".join([str(randint(1, 100)) for _ in range(1000)]))
    file.seek(0)
    print(sum(map(int, file.readline().split())))
