from functools import partial, reduce
from operator import add, mul


original_numbers = (1, 2, 3)
extended_numbers = original_numbers + (4,)
print("1. Tuple with new number:", extended_numbers)



mixed_numbers = (1, 2, [3, 4], 5)
mixed_numbers[2][1] = 99
print("2. After changing inner list:", mixed_numbers)


fruit_tuple = ("apple", "banana", "cherry")
fruit_list = list(fruit_tuple)
fruit_list.append("mango")
fruit_tuple = tuple(fruit_list)
print("3. Fruits with mango:", fruit_tuple)


a, b, *rest = (10, 20, 30, 40)
print("4. a =", a, "| b =", b, "| rest =", rest)


# 2D lists 


def sum_each_row(matrix):
    return list(map(sum, matrix))



def sum_each_column(matrix):
    return list(map(sum, zip(*matrix)))


sample_matrix = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print("\n--- 2D lists ---")
print("Row sums:", sum_each_row(sample_matrix))
print("Column sums:", sum_each_column(sample_matrix))


#Helper functions (no lambda) 

def is_even(number):
    return number % 2 == 0


def is_longer_than(min_length, word):
    return len(word) > min_length


def first_value_above(threshold, pair):
    return pair[0] > threshold


def is_divisible_by_three_and_five(number):
    return number % 3 == 0 and number % 5 == 0


def is_palindrome(word):
    return word == word[::-1]


def is_greater_than(threshold, value):
    return value > threshold


def square(number):
    return number * number


def add_tax(price, tax_rate):
    return round(price * (1 + tax_rate), 2)


def join_with_space(left_text, right_text):
    return f"{left_text} {right_text}"


# Part 3: filter()

print("\n--- filter() ---")


even_numbers = list(filter(is_even, range(1, 21)))
print("1. Even numbers:", even_numbers)



def get_long_words(words, min_length=5):
    return list(filter(partial(is_longer_than, min_length), words))


print("2. Long words:", get_long_words(["cat", "elephant", "tiger", "lion"]))


pairs = [(1, "A"), (4, "B"), (2, "C")]
print("3. First value > 2:", list(filter(partial(first_value_above, 2), pairs)))


divisible_numbers = list(filter(is_divisible_by_three_and_five, range(1, 51)))
print("4. Divisible by 3 and 5:", divisible_numbers)


words_to_check = ["level", "world", "madam", "python"]
print("5. Palindromes:", list(filter(is_palindrome, words_to_check)))


#Part 4: map()

print("\n--- map() ---")


print("1. Uppercase:", list(map(str.upper, ["python", "java", "c++"])))


print("2. Squares:", list(map(square, range(1, 11))))


print("3. Capitalized:", list(map(str.capitalize, ["john", "mary", "steve"])))


prices = [100, 200, 300]
prices_with_tax = list(map(partial(add_tax, tax_rate=0.10), prices))
print("4. Prices with 10% tax:", prices_with_tax)


#Part 5: reduce()

print("\n--- reduce() ---")


print("1. Sum 1 to 50:", reduce(add, range(1, 51)))


print("2. Maximum:", reduce(max, [3, 5, 9, 2, 8]))


print("3. Sentence:", reduce(join_with_space, ["I", "love", "Python"]))


print("4. Product of squares:", reduce(mul, map(square, [1, 2, 3, 4])))


#Part 6: Combined

print("\n--- Combined ---")



def sums_greater_than(tuples, threshold=5):
    tuple_sums = map(sum, tuples)
    return list(filter(partial(is_greater_than, threshold), tuple_sums))


print("1. Sums > 5:", sums_greater_than([(1, 2), (3, 4), (5, 6)]))



def total_of_numeric_strings(data):
    numeric_strings = filter(str.isdigit, data)
    return sum(map(int, numeric_strings))


print("2. Total:", total_of_numeric_strings(["123", "456", "789", "abc", "def"]))
