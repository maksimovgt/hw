# income = float(input('выручка фирмы: '))
# costs = float(input('издержки фирмы: '))
#
# if income > costs:
#     profit = int((income / costs) * 100)
#     print('фирма прибыльна, рентабельность:', profit,'%')
#     n = int(input('введите численность сотрудников: '))
#     p = profit / n
#     print('прибыль на сотрудника:', p,'%')
#
# else:
#     print('Фирма в убытке')

revenue = float(input("Введите значение выручки - "))
costs = float(input("Введите значение издержек - "))
result = revenue - costs

if result > 0:
    print(f"Ваша компания работает с прибылью {result}!")
    print(f"Рентабельность выручки составила - {result/revenue:.3f}")
    persons = int(input("Введите кол-во сотрудников в компании - "))
    print(f"Прибыль на одного сотрудника - {result/persons:.3f}")
elif result < 0:
    print(f"Ваша компания в убытке - {-result}")
else:
    print("Ваша компания работает в ноль")

