with open('salary.txt','r') as file:
    workers = {line.split()[0]: float(line.split()[1]) for line in file}

print(f'Средняя зарплата: {round(sum(workers.values())) / len(workers)}')
print(f'Зарплата меньше 20к: {[el[0] for el in workers.items() if el[1] < 20000]}')
