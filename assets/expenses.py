import sqlite3
from db import *

expenses = []

def add_expense():
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    expense_name = input("Enter expense description: ").lower()
    try: 
        expense_amount = float(input("Enter the expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number: ")
    try:
        cursor.execute("INSERT INTO tbl_expenses (name, amount) VALUES (?, ?)", (expense_name, expense_amount))
        print(f"Expense '{expense_name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"{expense_name} already exists. No duplicate values allowed")
    conn.commit()
    conn.close()
    

# Function to view all expenses
def view_expenses():
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    try: 
        cursor.execute("SELECT * FROM tbl_expenses")
        all_expenses = cursor.fetchall()
        if all_expenses:
            for exp in all_expenses:
                print(f"ID: {exp[0]}, Name: {exp[1]}, Amount: {exp[2]}")
        else:
            print("No expenses found")
    except Exception as e:
        print(e)

    conn.close()
    

# Function to edit an existing expense
def edit_expense():
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    expense_id = int(input("enter ID of the expense to edit: "))
    try:
        cursor.execute("SELECT * FROM tbl_expenses WHERE id = ?", (expense_id,))
        result = cursor.fetchone()
        if result:
            print(f"You chose {result[1]} : {result[2]}")
            new_amount = float(input(f"Enter new expense amount for {result[1]}: "))
            cursor.execute("UPDATE tbl_expenses SET amount = ? WHERE id = ?", (new_amount, expense_id))
            conn.commit()
            print(f"Expense '{result[1]}' updated successfully to {new_amount}.")
        else:
            print("Expense ID not found. Please enter a valid ID.")
    except Exception as e:
        print(e)
        
    conn.close()


# Function to delete an expense
def delete_expense():
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    expense_id = int(input("Enter the ID of the tbl_expense to delete: "))
    try: 
        cursor.execute("SELECT * FROM tbl_expenses WHERE id = ?", (expense_id,))
        result = cursor.fetchone()
        if result:
            print(f"you chose {result[1]}")
            cursor.execute("DELETE FROM tbl_expenses WHERE id = ?", (expense_id,))
            conn.commit()
            print(f"Expense '{result[1]}' deleted")
        else:
            print("Expense ID not found. Please enter a valid ID.")
    except Exception as e:
        print(e)
    
    conn.close()
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