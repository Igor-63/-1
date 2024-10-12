data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]




def calculate_structure_sum(struct):

    int_sum=0
    if isinstance(struct, int):
        return struct
    if isinstance(struct, str):
        return len(struct)


    for i in struct:
       if  isinstance(struct, dict):
           int_sum = int_sum + calculate_structure_sum(i) + calculate_structure_sum(struct[i])
       else:
           int_sum = int_sum + calculate_structure_sum(i)

    return int_sum

result = calculate_structure_sum(data_structure)
print(result)






