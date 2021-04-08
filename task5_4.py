<<<<<<< HEAD
dict1 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
new_file = []
with open('file4.txt', 'r', encoding='utf-8') as file1:
    for i in file1:
        i = i.split(' ', 1)
        new_file.append(dict1[i[0]] + '  ' + i[1])
    print(new_file)

with open('file4new.txt', 'w', encoding='utf-8') as file2:
    file2.writelines(new_file)
=======
new_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('eng.txt','r', encoding='utf-8') as file, open('rus.txt', 'w', encoding='windows-1251') as new_file:
    new_file.write(str([line.replace(line.split()[0], new_dict.get(line.split()[0])) for line in file]))
>>>>>>> c8c3163a9f2a883b886540e64a6e22b3f347819a
