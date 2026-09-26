number = 8342917
n = abs(number)
digit_count = 0
if n == 0:
    digit_count = 1
while n > 0:
    digit_count += 1
    n //= 10
print(digit_count, "\n")
