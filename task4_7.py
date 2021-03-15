def factorial(num):
    fac_num = 1
    if num == 0:
        yield f'{num}! = 1'
    for i in range(1, num + 1):
        fac_num *= i
        yield f'{i}! = {fac_num}'


for el in factorial(int(input('Факториал числа - '))):
    print(el)
#на проверку