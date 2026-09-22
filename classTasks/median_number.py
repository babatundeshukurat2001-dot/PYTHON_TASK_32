a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

numbers = [a, b, c, d]
numbers.sort()

median = (numbers[1] + numbers[2]) / 2
print(f"Median: {int(median)}")


total = a + b + c + d
print(f"Sum: {total}")


mean = total // 4
print(f"Mean: {mean}")



