with open('file1.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Введите строку: ')
        if not line:
            break
        file.write(f'{line}\n')