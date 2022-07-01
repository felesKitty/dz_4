from random import randint

ex_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_of_n = [randint(-10, 10) for n in ex_list]
result_list = [v for v in list_of_n if list_of_n.count(v) <= 1]
print(f'First list {list_of_n}\nResult {result_list}')
