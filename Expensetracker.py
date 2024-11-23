import json
import os

# File to store the expense data
FILE_NAME = "expenses.json"

# Load existing data or create a new file
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add a new expense
def add_expense(data):
    try:
        name = input("Enter expense name: ").strip()
        amount = float(input("Enter expense amount: ").strip())
        category = input("Enter category (optional): ").strip()
        data.append({"name": name, "amount": amount, "category": category})
        save_data(data)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")

# View all expenses
def view_expenses(data):
    if not data:
        print("No expenses recorded yet.")
        return

    total = 0
    print("\nExpense List:")
    print(f"{'ID':<5} {'Name':<20} {'Amount':<10} {'Category':<15}")
    print("-" * 50)
    for idx, expense in enumerate(data, 1):
        print(
            f"{idx:<5} {expense['name']:<20} {expense['amount']:<10.2f} {expense['category']:<15}"
        )
        total += expense["amount"]

    print("-" * 50)
    print(f"Total Expenses: {total:.2f}\n")

# Delete an expense
def delete_expense(data):
    view_expenses(data)
    try:
        expense_id = int(input("Enter the ID of the expense to delete: "))
        if 1 <= expense_id <= len(data):
            removed = data.pop(expense_id - 1)
            save_data(data)
            print(f"Deleted expense: {removed['name']} - {removed['amount']:.2f}")
        else:
            print("Invalid ID. No changes made.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Main program loop
def main():
    data = load_data()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            delete_expense(data)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
