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
    def test_visa(self):
        self.assertEqual(get_card_type("4388576018410707"), "Visa")

    def test_mastercard(self):
        self.assertEqual(get_card_type("5399831619690403"), "MasterCard")

    def test_american_express(self):
        self.assertEqual(get_card_type("378282246310005"), "American Express")

    def test_discover(self):
        self.assertEqual(get_card_type("6011111111111117"), "Discover")

    def test_unknown_prefix(self):
        self.assertEqual(get_card_type("234319283049582"), "Invalid Card")

    def test_prefix_3_without_7_is_not_amex(self):
        self.assertEqual(get_card_type("341111111111111"), "Invalid Card")


class LuhnStepsTest(unittest.TestCase):
    """Numbers from the worked example in the brief."""

    def test_double_even_places_sum(self):
        self.assertEqual(sum_of_double_even_places("4388576018402626"), 37)

    def test_odd_places_sum(self):
        self.assertEqual(sum_of_odd_places("4388576018402626"), 38)

    def test_invalid_example_fails_luhn(self):
        self.assertFalse(passes_luhn_check("4388576018402626"))

    def test_valid_example_passes_luhn(self):
        self.assertTrue(passes_luhn_check("4388576018410707"))


class IsValidTest(unittest.TestCase):
    def test_valid_mastercard_from_brief(self):
        self.assertTrue(is_valid("5399831619690403"))

    def test_invalid_mastercard_from_brief(self):
        self.assertFalse(is_valid("5399831619690404"))

    def test_invalid_card_from_brief(self):
        self.assertFalse(is_valid("234319283049582"))

    def test_valid_amex(self):
        self.assertTrue(is_valid("378282246310005"))

    def test_too_short(self):
        # Passes Luhn but has only 12 digits.
        self.assertFalse(is_valid("400000000008"))

    def test_too_long(self):
        # Passes Luhn but has 17 digits.
        self.assertFalse(is_valid("40000000000000006"))

    def test_non_digits(self):
        self.assertFalse(is_valid("4388-5760-1841-0707"))
        self.assertFalse(is_valid("abcdefghijklmnop"))

    def test_empty(self):
        self.assertFalse(is_valid(""))


class FormatResultTest(unittest.TestCase):
    def test_valid_output(self):
        banner = "*" * 40
        expected = "\n".join(
            [
                banner,
                "**Credit Card Type: MasterCard",
                "**Credit Card Number: 5399831619690403",
                "**Credit Card Digit Length: 16",
                "**Credit Card Validity Status: Valid",
                banner,
            ]
        )
        self.assertEqual(format_result("5399831619690403"), expected)

    def test_invalid_card_output(self):
        output = format_result("234319283049582")
        self.assertIn("**Credit Card Type: Invalid Card", output)
        self.assertIn("**Credit Card Digit Length: 15", output)
        self.assertIn("**Credit Card Validity Status: Invalid", output)


if __name__ == "__main__":
    unittest.main()
