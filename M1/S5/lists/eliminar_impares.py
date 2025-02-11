my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in my_list[:]:
    if (i % 2 == 1):
        my_list.remove(i)
print(my_list)