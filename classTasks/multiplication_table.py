print("\t\tMultiplication Table")


for count in range(1, 10):

    print(f"{count:3}", end=" ")


print("\t\t\t\t\t\t\t\t\t---------------------------------")

for count in range(1, 10):
    
    print(f"{count} |", end="")

    for index in range(1, 10):

        print(f"{count*index:3}", end=" ")

    print()




