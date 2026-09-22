number = int(input("Enter a five-digit integer: "))

digit1 = number // 10000
digit2 = number // 1000 % 10
digit4 = number // 10 % 10
digit5 = number % 10

if digit1 == digit5 and digit2 == digit4:
    print("Palindrome")
else:
    print("Not a palindrome")
