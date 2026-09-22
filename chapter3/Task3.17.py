#a

for row in range(1, 11):
    for column in range(row):
        print('*', end='')
    print()

#b

for row in range(10, 0, -1):
    for column in range(row):
        print('*', end='')
    print()
   
#c

for row in range(10, 0, -1):
    for space in range(10 - row):
        print(' ', end='')

    for column in range(row):
        print('*', end='')

    print()


#d

for row in range(1, 11):

    for space in range(10 - row):
        print(' ', end='')

    for column in range(row):
        print('*', end='')

    print()
