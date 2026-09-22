passes = 0
students = 10

for student in range(students):

    result = int(input("Enter result (1=pass, 2=fail): "))

    while result != 1 and result != 2:
        print("Invalid input. Enter 1 or 2.")
        result = int(input("Enter result (1=pass, 2=fail): "))

    if result == 1:
        passes += 1

failures = students - passes

print("Number of passes:", passes)
print("Number of failures:", failures)
