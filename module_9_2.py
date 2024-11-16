first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(rez2)
                for rez2 in first_strings
                    if len(rez2)>5]

second_result = [(first, second)
                 for first in first_strings
                    for  second in second_strings
                        if len(first) == len(second)]


third_result = [{first:len(first)}
                 for first in (first_strings + second_strings)
                    if ( not len(first) % 2)]




print(first_result)
print(second_result)
print(third_result)