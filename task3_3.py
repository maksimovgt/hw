def my_func(arg1, arg2, arg3):
    mylist = [arg1, arg2, arg3]
    mylist.remove(min(mylist))
    return sum(mylist)

print(my_func(1, 2, 3))