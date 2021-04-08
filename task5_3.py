<<<<<<< HEAD
with open('file3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'средний месячный оклад: {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'сотрудники с  окладом меньше 20 тыс: {[e[0] for e in employees_dict.items() if e[1] < 20000]}')
=======
with open('salary.txt','r') as file:
    workers = {line.split()[0]: float(line.split()[1]) for line in file}

print(f'Средняя зарплата: {round(sum(workers.values())) / len(workers)}')
print(f'Зарплата меньше 20к: {[el[0] for el in workers.items() if el[1] < 20000]}')
>>>>>>> c8c3163a9f2a883b886540e64a6e22b3f347819a
