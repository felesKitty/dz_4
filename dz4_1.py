from sys import argv


def wages():
    try:
        time, rate, prize = map(float, argv[1:])
        print(f'Your wages = {time + rate + prize}')
    except ValueError:
        print(f'Please, enter 3 only numbers')


wages()
