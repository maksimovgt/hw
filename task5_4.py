dict1 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
new_file = []
with open('file4.txt', 'r', encoding='utf-8') as file1:
    for i in file1:
        i = i.split(' ', 1)
        new_file.append(dict1[i[0]] + '  ' + i[1])
    print(new_file)

with open('file4new.txt', 'w', encoding='utf-8') as file2:
    file2.writelines(new_file)