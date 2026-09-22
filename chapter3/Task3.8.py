numbers = []

for i in range(4):
    number = int(input("Enter an integer: "))
    numbers.append(number)

total = sum(numbers)
average = total / len(numbers)
product = 1

for number in numbers:
    product *= number

print("Sum:", total)
print("Average:", average)
print("Product:", product)
print("Smallest:", min(numbers))
print("Largest:", max(numbers))
