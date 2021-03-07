l1 = list(input("Введите элементы через пробел - ").split())

i = 0
while i + 1 < len(l1):
    if i % 2 == 0:
        l1.insert(i, l1.pop(i + 1))
    i += 1
print(l1)

#на проверку