my_list = list(range(1, 7))
print(my_list)
for index, item in enumerate(my_list):
    print(list(enumerate(my_list)))
    my_list.pop(index)
print(my_list)
