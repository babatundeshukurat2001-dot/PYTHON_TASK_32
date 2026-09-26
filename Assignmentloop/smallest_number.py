number = 8342917
n = abs(number)
smallest = 9
while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10
print(smallest)
 


