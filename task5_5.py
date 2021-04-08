from random import randint
<<<<<<< HEAD
with open('file5.txt', mode='w+', encoding='utf-8') as file:
    file.write(" ".join([str(randint(1, 100)) for _ in range(1000)]))
=======

with open('numbers.txt', 'w+') as file:
    file.write(' '.join([str(randint(1, 10)) for el in range(100)]))
>>>>>>> c8c3163a9f2a883b886540e64a6e22b3f347819a
    file.seek(0)
    print(sum(map(int, file.readline().split())))
