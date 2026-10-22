import unittest

from credit_card_validator import (
    format_result,
    get_card_type,
    is_valid,
    passes_luhn_check,
    sum_of_double_even_places,
    sum_of_odd_places,
)

class CardTypeTest(unittest.TestCase):
    def test_number_starting_with_4_is_visa(self):
        card_number = "4388576018410707"

        actual_card_type = get_card_type(card_number)

        self.assertEqual(actual_card_type, "Visa")

    def test_number_starting_with_5_is_mastercard(self):
        card_number = "5399831619690403"

        actual_card_type = get_card_type(card_number)

        self.assertEqual(actual_card_type, "MasterCard")

    def test_number_starting_with_37_is_american_express(self):
        card_number = "378282246310005"

        actual_card_type = get_card_type(card_number)

        self.assertEqual(actual_card_type, "American Express")

    def test_number_starting_with_6_is_discover(self):
        card_number = "6011111111111117"

        actual_card_type = get_card_type(card_number)

        self.assertEqual(actual_card_type, "Discover")

    def test_number_with_unknown_prefix_is_invalid_card(self):
        card_number = "234319283049582"

        actual_card_type = get_card_type(card_number)

        self.assertEqual(actual_card_type, "Invalid Card")

    def test_number_starting_with_3_but_not_37_is_not_american_express(self):
        card_number = "341111111111111"

        actual_card_type = get_card_type(card_number)

        self.assertEqual(actual_card_type, "Invalid Card")


class LuhnStepsTest(unittest.TestCase):
    def test_sum_of_double_even_places(self):
        card_number = "4388576018402626"

        actual_sum = sum_of_double_even_places(card_number)

        self.assertEqual(actual_sum, 37)

    def test_sum_of_odd_places(self):
        card_number = "4388576018402626"

        actual_sum = sum_of_odd_places(card_number)

        self.assertEqual(actual_sum, 38)

    def test_card_with_bad_checksum_fails_luhn_check(self):
        card_number = "4388576018402626"

        result = passes_luhn_check(card_number)

        self.assertFalse(result)

    def test_card_with_good_checksum_passes_luhn_check(self):
        card_number = "4388576018410707"

        result = passes_luhn_check(card_number)

        self.assertTrue(result)


class IsValidTest(unittest.TestCase):
    def test_valid_mastercard_is_valid(self):
        card_number = "5399831619690403"

        self.assertTrue(is_valid(card_number))

    def test_mastercard_with_wrong_last_digit_is_not_valid(self):
        card_number = "5399831619690404"

        self.assertFalse(is_valid(card_number))

    def test_card_with_unknown_prefix_is_not_valid(self):
        card_number = "234319283049582"

        self.assertFalse(is_valid(card_number))

    def test_valid_american_express_is_valid(self):
        card_number = "378282246310005"

        self.assertTrue(is_valid(card_number))

    def test_number_with_too_few_digits_is_not_valid(self):
        card_number_with_12_digits = "400000000008"

        self.assertFalse(is_valid(card_number_with_12_digits))

    def test_number_with_too_many_digits_is_not_valid(self):
        card_number_with_17_digits = "40000000000000006"

        self.assertFalse(is_valid(card_number_with_17_digits))

    def test_number_with_dashes_is_not_valid(self):
        card_number_with_dashes = "4388-5760-1841-0707"

        self.assertFalse(is_valid(card_number_with_dashes))

    def test_number_made_of_letters_is_not_valid(self):
        card_number_with_letters = "abcdefghijklmnop"

        self.assertFalse(is_valid(card_number_with_letters))

    def test_empty_string_is_not_valid(self):
        empty_card_number = ""

        self.assertFalse(is_valid(empty_card_number))



class FormatResultTest(unittest.TestCase):
    def test_result_for_a_valid_card(self):
        card_number = "5399831619690403"
        border_line = "*" * 40
        expected_output = "\n".join(
            [
                border_line,
                "**Credit Card Type: MasterCard",
                "**Credit Card Number: 5399831619690403",
                "**Credit Card Digit Length: 16",
                "**Credit Card Validity Status: Valid",
                border_line,
            ]
        )

        actual_output = format_result(card_number)

        self.assertEqual(actual_output, expected_output)

    def test_result_for_an_invalid_card_shows_invalid_type(self):
        card_number = "234319283049582"

        actual_output = format_result(card_number)

        self.assertIn("**Credit Card Type: Invalid Card", actual_output)

    def test_result_for_an_invalid_card_shows_digit_length(self):
        card_number = "234319283049582"

        actual_output = format_result(card_number)

        self.assertIn("**Credit Card Digit Length: 15", actual_output)

    def test_result_for_an_invalid_card_shows_invalid_status(self):
        card_number = "234319283049582"

        actual_output = format_result(card_number)

        self.assertIn("**Credit Card Validity Status: Invalid", actual_output)


if __name__ == "__main__":
    unittest.main()
