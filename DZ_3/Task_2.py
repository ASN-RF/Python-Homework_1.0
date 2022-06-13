from os import system


system('cls')

def sum_of_odd_elems(lst, sum_el: int = 0):
    for item in range(1, len(lst), 2):
        sum_el += lst[item]
    return sum_el


my_list = [2, 3, 5, 9, 3]
print(f'{my_list} -> {sum_of_odd_elems(my_list)}')

my_list = [2, 3, 5, 9, 3, 4]
print(f'{my_list} -> {sum_of_odd_elems(my_list)}')