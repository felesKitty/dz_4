from itertools import cycle

print('Cycle: ')
iter_list = ['qwerty', 484, 38, 11.11]
iter_2 = cycle(iter_list)
for v in range(len(iter_list) * 5):
    print(next(iter_2), end=' ')
