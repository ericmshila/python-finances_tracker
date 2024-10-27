import sqlite3
# from db import *
def init_db():
    try:
        conn = sqlite3.connect("expenses.db")
    except sqlite3.Error as e:
        print(e)
    cursor = conn.cursor()
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tbl_expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount REAL NOT NULL)
    """)
    conn.commit()
    conn.close()
    print("Database initialized and table created")

expenses = []

def add_expense():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    expense_name = input("Enter expense description: ")
    try: 
        expense_amount = float(input("Enter the expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number: ")
    cursor.execute("INSERT INTO expenses (name, amount) VALUES (?, ?)", (expense_name, expense_amount))
    conn.commit()
    conn.close()
    print(f"Expense '{expense_name}' added successfully.")

# Function to view all expenses
def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    all_expenses = cursor.fetchall()
    conn.close()
    if all_expenses:
        for exp in expenses:
            print(f"ID: {exp[0]}, Name: {exp[1]}, Amount: {exp[2]}")
    else:
        print("No expenses found")
# Function to edit an existing expense
def edit_expense():
    view_expenses()
    try:
        index = int(input("Enter the number of the expense to edit: ")) - 1
        if index < 0 or index >= len(expenses):
            print("Invalid expense number.")
            return
        
        # Ask if user wants to change name, amount, or both
        change_name = input("Do you want to change the name? (yes/no): ").strip().lower()
        if change_name == 'yes':
            new_name = input("Enter the new name for the expense: ")
        else:
            new_name = expenses[index]["name"]  # Keep the original name

        change_amount = input("Do you want to change the amount? (yes/no): ").strip().lower()
        if change_amount == 'yes':
            try:
                new_amount = float(input("Enter the new amount for the expense: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                return
        else:
            new_amount = expenses[index]["amount"]  # Keep the original amount

        # Update the expense with the new values
        expenses[index] = {"name": new_name, "amount": new_amount}
        print(f"Expense updated successfully.")

    except ValueError:
        print("Invalid input.")

# Function to delete an expense
def delete_expense():
    view_expenses()
    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if index < 0 or index >= len(expenses):
            print("Invalid expense number.")
            return
        
        removed = expenses.pop(index)
        print(f"Expense '{removed['name']}' removed successfully.")
    except ValueError:
        print("Invalid input.")

# Simple CLI menu
def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            edit_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Exiting the program. Goodbye!!!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    init_db()
    main()