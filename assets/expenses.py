import sqlite3
from db import *

conn = sqlite3.connect("transactions.db")
cursor = conn.cursor()

def close_connection():
    conn.close()


def add_expense():
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


# Function to view all expenses
def view_expenses():
    try: 
        cursor.execute("SELECT * FROM tbl_expenses")
        all_expenses = cursor.fetchall()
        if all_expenses:
            for exp in all_expenses:
                print(f"ID: {exp[0]} | Name: {exp[1]} | Amount: {exp[2]}")
        else:
            print("No expenses found")
    except Exception as e:
        print(e)
    

# Function to edit an existing expense
def edit_expense():
    while True:
        print("You chose the edit option")
        print("---------------------------------------------------")
        view_expenses()
        print("---------------------------------------------------")
        print("Enter num 0 to return to te previous menu")
        print("Otherwise, Enter ID of expense to edit")
        expense_id = int(input("Enter of the expense to edit: "))
        if expense_id == 0:
            print("Bye!!!")
            break
        else:
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


# Function to delete an expense
def delete_expense():
    while True:
        print("Delete from the list of expenses below")
        print("Enter num 0 to return to te previous menu")
        view_expenses()
        expense_id = int(input("Enter the ID of the expense to delete: "))
        if expense_id == 0:
            print("Bye")
            break
        else:
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
