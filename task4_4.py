from random import randint
my_list = [randint(0, 10) for el in range(50)]
new_list = [el for el in my_list if el % 2 == 0]
print(my_list)
print(new_list)