n = int(input('Введите номер месяца от 1 до 12 - '))

season = {
    1: 'зима',
    2: 'весна',
    3: 'лето',
    4: 'осень'
}
months = ['', 'декабрь', 'январь', 'февраль', 'март', 'апрель', 'май',
          'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', ]

if n in range(1, 3):
    print(f'Сезон выбранного месяца - {season.get(1)}')
else:
    print('Error')
if n in range(4, 6):
    print(f'Сезон выбранного месяца - {season.get(2)}')
else:
    print('Error')
if n in range(7, 9):
    print(f'Сезон выбранного месяца - {season.get(3)}')
else:
    print('Error')
if n in range(10, 12):
    print(f'Сезон выбранного месяца - {season.get(4)}')
else:
    print('Error')

# на проверку