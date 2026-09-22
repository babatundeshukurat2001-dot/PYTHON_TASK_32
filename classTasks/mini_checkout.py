print("===== MINI CHECKOUT SYSTEM =====")

name = input("Enter your name:  ")

total = 0


while True:

    product_name = input("Enter product name: ")

    
    price = float(input(f"Enter price of {product_name}: "))

    
    quantity = int(input(f"Enter quantity of {product_name}: "))

    
    amount = quantity * price


    total = total + amount

    
    response = input("Do you want to continue? (yes/no): ")

    
    if response.lower() == "no":
        break

print("\n==== RECEIPT ====")

print(f"Total amount to pay: ₦{total:,.2f}") 
