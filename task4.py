# n = int(input('Введите целое положительное число: '))
# m = n % 10
# n = n // 10
#
# while n > 10:
#     if n % 10 > m:
#         m = n % 10
#     n = n // 10
# print(m)

num_init = int(input("введите целое положительное число - "))
maximum = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit
    if digit == 9:
        break

    num = num // 10
    print(num)

print(f"Наибольшая цифра в числе {num_init} равна {maximum}")