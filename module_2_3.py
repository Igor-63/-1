my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_my_list = len(my_list)
my_index = 0

while my_index < len_my_list:
    if my_list[my_index] >= 0:
        print(my_list[my_index])
        my_index = my_index + 1
