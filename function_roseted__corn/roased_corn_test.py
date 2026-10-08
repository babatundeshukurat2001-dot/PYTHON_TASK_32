import unittest

from functions import (
    string_length, first_last_two, add_ing, longest_word,
    remove_odd_index_chars, keep_odd_index_chars, find_min, find_max,
    repeat_string, square_list, sum_of_squares,
)

class TestStringLength(unittest.TestCase):
    def test_normal_word(self):
        self.assertEqual(string_length("semicolon"), 9)

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)


class TestFirstLastTwo(unittest.TestCase):
    def test_normal_word(self):
        self.assertEqual(first_last_two("semicolon"), "seon")

    def test_two_letters(self):
        self.assertEqual(first_last_two("on"), "onon")

    def test_too_short(self):
        self.assertEqual(first_last_two("o"), "")


class TestAddIng(unittest.TestCase):
    def test_add_ing(self):
        self.assertEqual(add_ing("abc"), "abcing")

    def test_already_ends_with_ing(self):
        self.assertEqual(add_ing("string"), "stringly")

    def test_too_short(self):
        self.assertEqual(add_ing("on"), "on")


class TestLongestWord(unittest.TestCase):
    def test_normal_list(self):
        words = ["welcome", "out", "weather", "mobile", "breakfast", "journey"]
        self.assertEqual(longest_word(words), ("breakfast", 9))

    def test_tie_returns_first(self):
        self.assertEqual(longest_word(["cat", "dog"]), ("cat", 3))

    def test_empty_list_raises_error(self):
        with self.assertRaises(ValueError):
            longest_word([])

class TestOddIndex(unittest.TestCase):
    def test_remove_odd(self):
        self.assertEqual(remove_odd_index_chars("semicolon"), "smcln")

    def test_keep_odd(self):
        self.assertEqual(keep_odd_index_chars("semicolon"), "eioo")


class TestFindMin(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(find_min([8, 4, 9, 2, 5, 7, 3]), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_min([-1, -5, 0]), -5)

    def test_empty_list_raises_error(self):
        with self.assertRaises(ValueError):
            find_min([])


class TestFindMax(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(find_max([8, 4, 9, 2, 5, 7, 3]), 9)

    def test_negative_numbers(self):
        self.assertEqual(find_max([-1, -5, -3]), -1)

    def test_empty_list_raises_error(self):
        with self.assertRaises(ValueError):
            find_max([])


class TestRepeatString(unittest.TestCase):
    def test_repeat_three_times(self):
        self.assertEqual(repeat_string("hello", 3), "hellohellohello")

    def test_repeat_zero_times(self):
        self.assertEqual(repeat_string("hi", 0), "")

    def test_negative_times(self):
        self.assertEqual(repeat_string("hi", -2), "")


class TestSquareList(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(square_list([2, 3, 4, 5, 7]), [4, 9, 16, 25, 49])

    def test_empty_list(self):
        self.assertEqual(square_list([]), [])


class TestSumOfSquares(unittest.TestCase):
    def test_normal_list(self):
        
        self.assertEqual(sum_of_squares([2, 3, 4, 5, 7]), 103)

    def test_empty_list(self):
        self.assertEqual(sum_of_squares([]), 0)



