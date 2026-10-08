def string_length(text):
    count = 0
    for _ in text:
        count += 1
    return count


def first_last_two(text):
    if len(text) < 2:
        return ""
    return text[:2] + text[-2:]


def add_ing(text):
    if len(text) < 3:
        return text
    if text.endswith("ing"):
        return text + "ly"
    return text + "ing"


def longest_word(words):
    if not words:
        raise ValueError("words must not be empty")
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest, len(longest)


def remove_odd_index_chars(text):
    return text[::2]


def keep_odd_index_chars(text):
    return text[1::2]


def find_min(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    smallest = numbers[0]
    for n in numbers[1:]:
        if n < smallest:
            smallest = n
    return smallest


def find_max(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")
    largest = numbers[0]
    for n in numbers[1:]:
        if n > largest:
            largest = n
    return largest


def repeat_string(text, times):
    if isinstance(times, float):
        return text
    return text * times


def square_list(numbers):
    return [n ** 2 for n in numbers]


def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += n ** 2
    return total
