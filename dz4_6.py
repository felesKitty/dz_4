from itertools import count

iter_1 = count(int(input('Enter any number for generator: ')))
print('First 15 numbers (from your number): ')
for v in range(15):
    print(next(iter_1), end='')
