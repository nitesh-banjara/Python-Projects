Product = []


while True:
    print("\n----- Inventory and Sales Management System -----")
    print("1. Add Product")
    print("2. Display all Product")
    print("3. Search for a Product")
    print("4. Update Product")
    print("5. Sell Product")
    print("6. View Low Stock Product")
    print("7. Total Revenew")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            prodect_id = int(input("Enter product id: "))
            product_name = input("Enter product name: ").strip()
            product_quantity = int(input("Enter product quantity: "))
            product_price = int(input("Enter total price of product: "))

            if prodect_id == "" or product_name == "":
                print("Product id and name cannot be empty!")
                continue
                if prodect_price =="" or prodect_quantity =="":
                    print("Product price and quantity cannot be empty! ")

            product_info_added = {
                "Product_id" : prodect_id,
                "Product_name" : product_name,
                "Product_quantity" : product_quantity,
                "Product_price" : product_price,
                "availability": True
            }

            Product.append(product_info_added)
            print("Product added successfully!")

            more_product = input("Do you want to add more? (yes/no): ").lower()

            if more_product != "yes":
                print("Thank you for adding books!")
                break

    if choice == "2":
        while True:
            print(product_info_added)
            break