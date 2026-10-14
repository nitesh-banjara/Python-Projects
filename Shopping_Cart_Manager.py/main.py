items = []

total_budget = int(input("Enter your total shopping budget: "))
shopping_cost = 0

while True:
    product_name = input("Enter product name: ")
    product_cost = int(input("Enter cost per piece: "))
    product_quantity = int(input("Enter quantity: "))

    total_cost = product_cost * product_quantity
    shopping_cost += total_cost

    product = {
        "product_name": product_name,
        "product_cost": product_cost,
        "product_quantity": product_quantity,
        "total_cost": total_cost
    }

    items.append(product)

    more_products = input("Do you want to add another product? (yes/no): ").lower()

    if more_products != "yes":
        print("\nThank you for shopping!")
        break

remaining_budget = total_budget - shopping_cost

print("\n========== SHOPPING SUMMARY ==========")

for product in items:
    print(f"Product Name: {product['product_name']}")
    print(f"Price per Piece: Rs. {product['product_cost']}")
    print(f"Quantity: {product['product_quantity']}")
    print(f"Total Cost: Rs. {product['total_cost']}")
    print("--------------------------------------")

print(f"Total Spending: Rs. {shopping_cost}")
print(f"Original Budget: Rs. {total_budget}")
print(f"Remaining Budget: Rs. {remaining_budget}")

print("======================================")
