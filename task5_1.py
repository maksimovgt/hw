with open('file.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Введите новую строку: ')
        if not line:
            break
        file.write(f'{line}\n')