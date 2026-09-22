e = 0
factorial = 1

for n in range(10):

    if n > 0:
        factorial *= n

    e += 1 / factorial

print("Approximation of e:", e)
