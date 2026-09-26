number = 8342917
n = abs(number)
largest = 0
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10
print(largest, "\n")

