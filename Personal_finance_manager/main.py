
transactions = []


def add_income():
    try:
        amount = float(input("Enter income amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()

        if not category or not description:
            print("Category and description cannot be empty.")
            return

        transactions.append({
            "amount": amount,
            "category": category,
            "description": description,
            "type": "income"
        })

        print("Income added successfully.")

    except ValueError:
        print("Please enter a valid number.")


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()

        if not category or not description:
            print("Category and description cannot be empty.")
            return

        transactions.append({
            "amount": amount,
            "category": category,
            "description": description,
            "type": "expense"
        })

        print("Expense added successfully.")

    except ValueError:
        print("Please enter a valid number.")


def view_transactions():
    if not transactions:
        print("No transactions found.")
        return

    print("\nAll Transactions")
    print("-" * 65)
    print(f"{'Type':<12}{'Amount':<12}{'Category':<18}{'Description'}")
    print("-" * 65)

    for transaction in transactions:
        print(
            f"{transaction['type'].title():<12}"
            f"{transaction['amount']:<12.2f}"
            f"{transaction['category']:<18}"
            f"{transaction['description']}"
        )


def view_summary():
    total_income = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "income"
    )

    total_expenses = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "expense"
    )

    balance = total_income - total_expenses

    print("\nFinancial Summary")
    print("-" * 30)
    print(f"Total Income:   {total_income:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")
    print(f"Remaining Balance: {balance:.2f}")

    expenses_by_category = {}

    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            expenses_by_category[category] = (
                expenses_by_category.get(category, 0)
                + transaction["amount"]
            )

    print("\nExpenses by Category")

    if not expenses_by_category:
        print("No expenses recorded.")
    else:
        for category, amount in expenses_by_category.items():
            print(f"{category}: {amount:.2f}")


def main():
    while True:
        print("\n===== Personal Finance Manager =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            print("Thank you for using Personal Finance Manager!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()
