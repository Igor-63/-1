calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(my_string):
    my_tuple = (len(my_string), my_string.upper(), my_string.lower())
    count_calls()
    return my_tuple


def is_contains(my_string, list_to_search):
    eq_string = False
    for i in list_to_search:
        if i.lower() == my_string.lower():
            eq_string = True
    count_calls()
    return eq_string


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
