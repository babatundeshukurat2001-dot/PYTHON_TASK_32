for row in range(1, 11):

    # Pattern A
    for column in range(row):
        print('*', end='')

    print(' ' * (10 - row), end='   ')

    # Pattern B
    for column in range(11 - row):
        print('*', end='')

    print(' ' * (row - 1), end='   ')

    # Pattern C
    print(' ' * (row - 1), end='')

    for column in range(11 - row):
        print('*', end='')

    print(' ' * (row - 1), end='   ')

    # Pattern D
    print(' ' * (10 - row), end='')

    for column in range(row):
        print('*', end='')

    print()
