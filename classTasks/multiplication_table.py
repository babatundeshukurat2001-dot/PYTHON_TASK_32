print("\t\tMultiplication Table")

#print("\t\t\t 1  2  3  4  5  6  7  8  9")

for count in range(1, 10):

    print(f"{count:3}", end=" ")


print("\t\t\t\t\t\t\t\t\t---------------------------------")

for count in range(1, 10):
    
    print(f"{count} |", end="")

    for index in range(1, 10):

        print(f"{count*index:3}", end=" ")

    print()




