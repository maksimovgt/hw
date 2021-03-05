# n = str(input('Введите число n: '))
# n2 = n + n
# n3 = n + n + n
# sum = int(n) + int(n2) + int(n3)
# print(sum)

n = input("введите положительное число")

while int(n) < 0:
    print("положительое число!")
    n = input("введите положительное число")
print(f"{n} + {n + n} + {n +n + n} = {int(n) + int(n + n) + int(n + n + n)}")