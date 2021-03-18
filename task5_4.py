new_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('eng.txt','r', encoding='utf-8') as file, open('rus.txt', 'w', encoding='windows-1251') as new_file:
    new_file.write(str([line.replace(line.split()[0], new_dict.get(line.split()[0])) for line in file]))