number = int(input("Enter a five-digit number: "))

divisor = 10000

for i in range(5):
    digit = number // divisor
    print(digit)

    number = number % divisor
    divisor //= 10
