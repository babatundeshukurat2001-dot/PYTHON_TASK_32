BANNER = "*" * 40


def get_card_type(card_number):
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
    total = 0
    last_position = len(card_number) - 1
    
    for position in range(last_position - 1, -1, -2):
        doubled_digit = int(card_number[position]) * 2
        if doubled_digit > 9:
            doubled_digit = doubled_digit // 10 + doubled_digit % 10
        total += doubled_digit
    return total


def sum_of_odd_places(card_number):
    total = 0
    last_position = len(card_number) - 1
    
    for position in range(last_position, -1, -2):
        total += int(card_number[position])
    return total


def passes_luhn_check(card_number):
    total = sum_of_double_even_places(card_number) + sum_of_odd_places(card_number)
    return total % 10 == 0


def is_valid(card_number):
    if not card_number.isdigit() or not card_number.isascii():
        return False
    if not 13 <= len(card_number) <= 16:
        return False
    if get_card_type(card_number) == "Invalid Card":
        return False
    return passes_luhn_check(card_number)


def format_result(card_number):
    validity_status = "Valid" if is_valid(card_number) else "Invalid"
    return "\n".join(
        [
            BANNER,
            f"**Credit Card Type: {get_card_type(card_number)}",
            f"**Credit Card Number: {card_number}",
            f"**Credit Card Digit Length: {len(card_number)}",
            f"**Credit Card Validity Status: {validity_status}",
            BANNER,
        ]
    )


    print("Hello, Kindly Enter Card details to verify")
    entered_card_number = input().strip()
    print(format_result(entered_card_number))
