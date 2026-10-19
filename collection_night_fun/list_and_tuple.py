
students = [
    ("Alice", 78),
    ("Bob", 45),
    ("Charlie", 90),
    ("Diana", 62),
    ("Kent", 30),
]

def print_students(student_list):
    for name, score in student_list:
        print(f"{name}: {score}")


def names_scoring_60_or_above(student_list):
    names = []
    for name, score in student_list:
        if score >= 60:
            names.append(name)
    return names


def count_passed(student_list, pass_mark=50):
    count = 0
    for name, score in student_list:
        if score >= pass_mark:
            count += 1
    return count


print("--- Students ---")
print_students(students)
print("Scored 60 or above:", names_scoring_60_or_above(students))
print("Number passed (mark 50):", count_passed(students))


# Products

products = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 45),
    ("Monitor", 300),
    ("USB Cable", 10),
]

def products_over_100(product_list):
    return list(filter(lambda item: item[1] > 100, product_list))


def total_price(product_list):
    total = 0
    for name, price in product_list:
        total += price
    return total


def print_products(product_list):
    for name, price in product_list:
        print(f"Product: {name} - Price: {price}")


print("\n--- Products ---")
print("Costing more than 100:", products_over_100(products))
print("Sum of all prices:", total_price(products))
print_products(products)


# Coordinates

points = [(2, 3), (-1, 4), (5, -6), (0, 7), (-3, -2)]


def both_positive(point_list):
    result = []
    for x, y in point_list:
        if x > 0 and y > 0:
            result.append((x, y))
    return result


positive_points = both_positive(points)
print("\n--- Coordinates ---")
print("Both values positive:", positive_points)


#Employees

employees = [
    ("John", "IT", 50000),
    ("Jane", "HR", 45000),
    ("Mike", "IT", 60000),
    ("Sara", "Finance", 70000),
]


def print_employees(employee_list):
    for name, department, salary in employee_list:
        print(f"{name} - {department} - {salary}")


def it_employees(employee_list):
    result = []
    for name, department, salary in employee_list:
        if department == "IT":
            result.append((name, department, salary))
    return result


def it_names_earning_over(employee_list, amount=55000):
    names = []
    for name, department, salary in it_employees(employee_list):
        if salary > amount:
            names.append(name)
    return names


print("\n--- Employees ---")
print_employees(employees)
print("IT employees:", it_employees(employees))
print("IT employees earning more than 55,000:")
for name in it_names_earning_over(employees):
    print(name)
