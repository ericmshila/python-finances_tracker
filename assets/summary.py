import sqlite3 
from db import *

def view_summary():
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    
    # Display income entries
    print("\nIncome Summary:")
    cursor.execute("SELECT name, amount FROM tbl_income")
    income_records = cursor.fetchall()
    if income_records:
        for name, amount in income_records:
            print(f"Income Source: {name}, Amount: {amount}")
    else:
        print("No income records found.")
    
    # Display expense entries
    print("\nExpenses Summary:")
    cursor.execute("SELECT name, amount FROM tbl_expenses")
    expense_records = cursor.fetchall()
    if expense_records:
        for name, amount in expense_records:
            print(f"Expense: {name}, Amount: {amount}")
    else:
        print("No expense records found.")
    
    conn.close()



def calculate_net_worth():
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    
    # Calculate total income
    cursor.execute("SELECT SUM(amount) FROM tbl_income")
    total_income = cursor.fetchone()[0] or 0  # Default to 0 if no income entries
    
    # Calculate total expenses
    cursor.execute("SELECT SUM(amount) FROM tbl_expenses")
    total_expenses = cursor.fetchone()[0] or 0  # Default to 0 if no expense entries
    
    # Calculate net worth
    net_worth = total_income - total_expenses
    
    # Display totals and net worth
    print("\n--- Financial Summary ---")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Net Worth (Current Balance): {net_worth}\n")
    
    conn.close()

    
view_summary()
calculate_net_worth()