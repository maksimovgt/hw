from sys import argv


def func_zp():
    try:
        hour, rate, bonus = map(int, argv[1:])
        return print(f"Зарплата будет - {(hour * rate) + bonus}")
    except ValueError:
        print("Введите ключи через пробел, часы зарплата бонус числами")


func_zp()
#на проверку