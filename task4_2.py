a = [11, 55, 33, 54, 24, 1, 3, 99, 100, 28, 54]
new_list = [a[el] for el in range(0, len(a)) if a[el] > a[el - 1]]
print(new_list)
#на проверку