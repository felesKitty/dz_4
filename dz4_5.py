from functools import reduce

def ex_list(elem_1, elem_2):
    return elem_1 * elem_2


our_list = [v for v in range(100, 1001, 2)]
print(f'{our_list}\n{reduce(ex_list, our_list)}')
