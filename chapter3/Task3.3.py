#The code contains nested for loops that print < or > depending on whether the row number is odd or even.

for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()
