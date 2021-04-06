with open('file3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'средний месячный оклад: {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'сотрудники с  окладом меньше 20 тыс: {[e[0] for e in employees_dict.items() if e[1] < 20000]}')