with open('my_file.txt', 'w') as file:
    while True:
        line = input('Введите строку: ')
        if not line:
            break
        file.write(f'{line}\n')