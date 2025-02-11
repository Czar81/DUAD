my_list = [4, 3, 6, 1, 7]
tmp = my_list[-1]
my_list[-1] = my_list[0]
my_list[0] = tmp
print(my_list)