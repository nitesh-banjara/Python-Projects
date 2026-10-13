Expenses = []

Total_Budget = int(input("Enter your total budget for expenses: "))
Total_spending = 0
 
while True:
    expense_name = input("Enter expense name: ")
    expense_amount = int(input("Enter expense amount: "))
    expense_category = input("Enter expense category: ")
    Total_spending = Total_spending + expense_amount
    expense = {
        "expenses_name": expense_name,
        "expenses_amount": expense_amount,
        "expenses_category": expense_category
    }

    Expenses.append(expense)

    another_expenses = input("Do you want to add another one also ? (yes/no): ").lower()

    if another_expenses != "yes":
        print("Thanks for you cooperation!")
        break

Remaining_budget = Total_Budget-Total_spending

for expense in Expenses:
    print(f"Expense: {expense['expenses_name']}, \nAmount: {expense['expenses_amount']}, \nCategory: {expense['expenses_category']}")

print(f"Total spending: {Total_spending}")
print(f"Remaining budget: {Remaining_budget}")
