pi = 0

for term in range(1, 1000000):
    denominator = 2 * term - 1

    if term % 2 == 1:
        pi += 4 / denominator
    else:
        pi -= 4 / denominator

    print(f"{term:7} {pi:.10f}")
