income = float(input('выручка фирмы: '))
costs = float(input('издержки фирмы: '))

if income > costs:
    profit = int((income / costs) * 100)
    print('фирма прибыльна, рентабельность:', profit,'%')
    n = int(input('введите численность сотрудников: '))
    p = profit / n
    print('прибыль на сотрудника:', p,'%')

else:
    print('Фирма в убытке')
