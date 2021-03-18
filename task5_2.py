c_lines = 0
c_words = 0

with open('file_str_count.txt', 'r') as file:
    for line in file:
        c_lines += 1
        words = line.split()
        c_words += len(words)

print(f'кол-во строк в файле {file.name} = {c_lines} и кол-во слов = {c_words} ')