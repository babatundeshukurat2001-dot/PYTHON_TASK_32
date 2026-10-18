"""Credit Card Validator (Semicolon - Arrays snacks).

Rules from the brief:
  * A card number has 13 to 16 digits.
  * It starts with 4 (Visa), 5 (MasterCard), 37 (American Express) or 6 (Discover).
  * It must pass the Luhn (Mod 10) check.
"""

BANNER = "*" * 40


def get_card_type(card_number):
    """Return the card type from the prefix, or 'Invalid Card'."""
    if card_number.startswith("37"):
        return "American Express"
    if card_number.startswith("4"):
        return "Visa"
    if card_number.startswith("5"):
        return "MasterCard"
    if card_number.startswith("6"):
        return "Discover"
    return "Invalid Card"


def sum_of_double_even_places(card_number):
    """Step 1 and 2: double every second digit from right to left.

    If doubling gives a two-digit number, add its digits together.
    Return the sum of those single-digit results.
    """
    total = 0
    # Start at the second digit from the right and move left in steps of 2.
    for i in range(len(card_number) - 2, -1, -2):
        doubled = int(card_number[i]) * 2
        total += doubled // 10 + doubled % 10 if doubled > 9 else doubled
    return total


def sum_of_odd_places(card_number):
    """Step 3: add the digits in the odd places from right to left."""
    total = 0
    for i in range(len(card_number) - 1, -1, -2):
        total += int(card_number[i])
    return total


def passes_luhn_check(card_number):
    """Step 4 and 5: the total must be divisible by 10."""
    total = sum_of_double_even_places(card_number) + sum_of_odd_places(card_number)
    return total % 10 == 0


def is_valid(card_number):
    """A card is valid if it is all digits, 13-16 long, has a known prefix
    and passes the Luhn check."""
    if not card_number.isdigit() or not card_number.isascii():
        return False
    if not 13 <= len(card_number) <= 16:
        return False
    if get_card_type(card_number) == "Invalid Card":
        return False
    return passes_luhn_check(card_number)


def format_result(card_number):
    """Build the output block shown in the brief."""
    card_type = get_card_type(card_number)
    status = "Valid" if is_valid(card_number) else "Invalid"
    return "\n".join(
        [
            BANNER,
            f"**Credit Card Type: {card_type}",
            f"**Credit Card Number: {card_number}",
            f"**Credit Card Digit Length: {len(card_number)}",
            f"**Credit Card Validity Status: {status}",
            BANNER,
        ]
    )


print("Hello, Kindly Enter Card details to verify")
card_number = input().strip()
print(format_result(card_number))
