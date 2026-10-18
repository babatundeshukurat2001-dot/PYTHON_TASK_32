import random

def create_random_list(size=10, low=1, high=50):

    return [random.randint(low, high) for _ in range(size)]


def get_length(items):
    count = 0
    for _ in items:
        count += 1
    return count


def sum_even_positions(items):
    total = 0
    position = 1
    for value in items:
        if position % 2 == 0:
            total += value
        position += 1
    return total


def sum_odd_positions(items):
    total = 0
    position = 1
    for value in items:
        if position % 2 == 1:
            total += value
        position += 1
    return total


def multiply_every_third(items):
    product = 1
    position = 1
    for value in items:
        if position % 3 == 0:
            product *= value
        position += 1
    return product


def average(items):
    size = get_length(items)
    if size == 0:
        raise ValueError("cannot take the average of an empty list")
    total = 0
    for value in items:
        total += value
    return total / size


def largest(items):
    if get_length(items) == 0:
        raise ValueError("empty list has no largest element")
    biggest = items[0]
    for value in items:
        if value > biggest:
            biggest = value
    return biggest


def smallest(items):
    if get_length(items) == 0:
        raise ValueError("empty list has no smallest element")
    least = items[0]
    for value in items:
        if value < least:
            least = value
    return least


def matching_strings(strings):
    return [s for s in strings if get_length(s) >= 2 and s[0] == s[-1]]


def count_matching_strings(strings):
    return get_length(matching_strings(strings))


# Part 2
def one_to_fifteen():
    return list(range(1, 16))


def sum_every_third(items):
    total = 0
    position = 1
    for value in items:
        if position % 3 == 0:
            total += value
        position += 1
    return total


def sum_first_middle_last(items):
    size = get_length(items)
    if size == 0:
        raise ValueError("empty list has no first, middle or last element")
    if size % 2 == 1:
        middle = items[size // 2]
    else:
        middle = (items[size // 2 - 1] + items[size // 2]) / 2
    return items[0] + middle + items[-1]


# Run
numbers = create_random_list()
print("Random list:", numbers)
print("Length (no len):", get_length(numbers))
print("Sum at even positions:", sum_even_positions(numbers))
print("Sum at odd positions:", sum_odd_positions(numbers))
print("Product at every third position:", multiply_every_third(numbers))
print("Average:", average(numbers))
print("Largest:", largest(numbers))
print("Smallest:", smallest(numbers))

words = ["level", "abc", "xyzx", "aa", "a", "noon"]
print("\nStrings:", words)
print("Matching strings:", matching_strings(words))
print("Count:", count_matching_strings(words))

sequence = one_to_fifteen()
print("\n1 to 15:", sequence)
print("Sum of every third element:", sum_every_third(sequence))
print("Sum of first, middle and last:", sum_first_middle_last(sequence))
