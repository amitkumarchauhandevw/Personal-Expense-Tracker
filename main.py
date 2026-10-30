import csv
import os

expenses = []

def save_expenses():
    with open("expenses.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "amount", "category", "date"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def load_expenses():
    if not os.path.exists("expenses.csv"):
        return

    with open("expenses.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)

def show_menu():
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Calculate Total Expenses")
    print("5. Monthly Summary")
    print("6. Delete Expense")
    print("0. Exit")


def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    # expenses.append(expense)
    # print("Expense added successfully!")
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    for expense in expenses:
        print("\n--------------------")
        print("Title:", expense["title"])
        print("Amount: Rs.", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])

def calculate_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expenses: Rs.", total)

def search_expenses():
    search_category = input("Enter category to search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            print("\n--------------------")
            print("Title:", expense["title"])
            print("Amount: Rs.", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])

            found = True

    if found == False:
        print("No expenses found in this category.")


def monthly_summary():
    month = input("Enter month (YYYY-MM): ")

    total = 0
    count = 0

    for expense in expenses:
        expense_month = expense["date"][:7]

        if expense_month == month:
            print("\n--------------------")
            print("Title:", expense["title"])
            print("Amount: Rs.", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])

            total = total + expense["amount"]
            count = count + 1

    if count == 0:
        print("No expenses found for this month.")
    else:
        print("\nMonthly Summary for", month)
        print("Number of expenses:", count)
        print("Total Expenses: Rs.", total)


def delete_expense():
    if len(expenses) == 0:
        print("No expenses available to delete.")
        return

    print("\n===== Delete Expense =====")

    for index, expense in enumerate(expenses, start=1):
        print(
            index, ".",
            expense["title"],
            "- Rs.", expense["amount"],
            "-", expense["category"]
        )

    try:
        choice = int(input("Enter expense number to delete: "))

        if choice < 1 or choice > len(expenses):
            print("Invalid expense number.")
            return

        deleted_expense = expenses.pop(choice - 1)
        save_expenses()

        print("Expense deleted successfully!")
        print("Deleted:", deleted_expense["title"])

    except ValueError:
        print("Please enter a valid number.")

load_expenses()
while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        # print("Search Expenses selected")
        search_expenses()

    elif choice == "4":
        # print("Calculate Total Expenses selected")
        calculate_total()

    elif choice == "5":
        # print("Monthly Summary selected")
        monthly_summary()

    elif choice == "6":
        # print("Delete Expense selected")
        delete_expense()

    elif choice == "0":
        print("Thank you for using the Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")




