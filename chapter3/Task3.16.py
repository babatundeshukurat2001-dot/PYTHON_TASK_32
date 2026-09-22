largest = None
second_largest = None

for i in range(10):

    number = int(input("Enter a number: "))

    if largest is None or number > largest:
        second_largest = largest
        largest = number

    elif second_largest is None or number > second_largest:
        second_largest = number

print("Largest:", largest)
print("Second largest:", second_largest)
