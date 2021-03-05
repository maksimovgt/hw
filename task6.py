# a = int(input('1 день кол-во км: '))
# b = int(input('общий результат км: '))
# d = 0
#
# while a < b:
#     a = a + (a * 0.1)
#     d = d + 1
# print(d)

while True:
    days = 1
    start_km = float(input("Начальный результат - "))
    last_km = float(input("Финальный результат - "))
    if start_km <= 0 or last_km < 0:
        print('Результаты должны быть больше нуля, стартовое значение не равно нулю')
    else:
        while start_km < last_km:
            start_km *= 1.1
            days += 1
        print(f"Спортсмен добьется результата за {days} дней")

# def km(res_min, res_max, days):
#     if res_min > res_max:
#         return days
#     else:
#         return km(res_min * 1.1, res_max, days + 1)
# print(km(int(input('Введите начальный результат'), int(input('Введите конечный результат')))))