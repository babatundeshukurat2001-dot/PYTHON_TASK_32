price = float(input("Enter purchase price: $"))

change = round((1 - price) * 100)

quarters = change // 25
change %= 25

dimes = change // 10
change %= 10

nickels = change // 5
change %= 5

pennies = change

print("Your change is:")

if quarters > 0:
    print(quarters, "quarter(s)")

if dimes > 0:
    print(dimes, "dime(s)")

if nickels > 0:
    print(nickels, "nickel(s)")

if pennies > 0:
    print(pennies, "penn(y/ies)")
