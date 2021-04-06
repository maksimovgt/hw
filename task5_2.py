lines = 0
words = 0

with open('file2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lines += 1
        word = line.split()
        words += len(word)

print(f'всего строк: {lines}  всего слов:{words}')