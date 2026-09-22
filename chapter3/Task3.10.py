principal = 1000
rate = 0.07

for year in range(1, 31):
    amount = principal * (1 + rate) ** year
    print(f"Year {year}: ${amount:.2f}")
