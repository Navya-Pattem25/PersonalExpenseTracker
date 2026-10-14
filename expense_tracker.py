
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if date == "":
        date = datetime.today().strftime("%Y-%m-%d")

    try:
        datetime.strptime(date, "%Y-%m-%d")
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        category = input("Enter category (Food, Travel, Shopping): ")
        description = input("Enter description: ")

        file_exists = os.path.exists(FILE_NAME)

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists or os.path.getsize(FILE_NAME) == 0:
                writer.writerow(["Date", "Amount", "Category", "Description"])

            writer.writerow([date, amount, category, description])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid date or amount!")


# View all expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for row in rows:
        print(" | ".join(row))


# Filter expenses by category
def filter_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    category = input("Enter category to search: ").strip().lower()
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n--- Filtered Expenses ---")
        for row in reader:
            if row["Category"].strip().lower() == category:
                print(row)
                found = True

    if not found:
        print("No expenses found in this category.")


# Display category-wise summary
def category_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    summary = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            summary[category] = summary.get(category, 0) + amount

    if not summary:
        print("No expenses recorded yet.")
        return

    print("\n--- Category Summary ---")
    for category, total in summary.items():
        print(f"{category}: Rs. {total:.2f}")


# Main menu
def main():
    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
