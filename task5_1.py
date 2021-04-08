<<<<<<< HEAD
with open('file1.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Введите новую строку: ')
=======
with open('my_file.txt', 'w') as file:
    while True:
        line = input('Введите строку: ')
>>>>>>> c8c3163a9f2a883b886540e64a6e22b3f347819a
        if not line:
            break
        file.write(f'{line}\n')