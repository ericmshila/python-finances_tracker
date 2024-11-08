import sqlite3
from db import *
from os import *

conn = sqlite3.connect("transactions.db")
cursor = conn.cursor()

def close_connection():
    conn.close()


def add_income():
    income_name = input("Enter income description: ").lower()
    try: 
        income_amount = float(input("Enter the income amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number: ")
    try:
        cursor.execute("INSERT INTO tbl_income (name, amount) VALUES (?, ?)", (income_name, income_amount))
        print(f"income '{income_name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"{income_name} already exists. No duplicate values allowed")
    conn.commit()
     

# Function to view all incomes
def view_income():
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    try: 
        cursor.execute("SELECT * FROM tbl_income")
        all_incomes = cursor.fetchall()
        if all_incomes:
            for exp in all_incomes:
                print(f"ID: {exp[0]} | Name: {exp[1]} | Amount: {exp[2]}")
        else:
            print("No incomes found")
    except Exception as e:
        print(e)

    

# Function to edit an existing income
def edit_income():
    while True:
        print("You chose the edit option.")
        print("---------------------------------------------------")
        view_income()
        print("---------------------------------------------------")
        print("Enter num 0 to return to te previous menu")
        print("Otherwise, Enter ID of income to edit")
        
        
        income_id = int(input("Enter of the income to edit: "))
        if income_id == 0:
            print("Bye!!!")
            break
        else:
            try:
                cursor.execute("SELECT * FROM tbl_income WHERE id = ?", (income_id,))
                result = cursor.fetchone()
                if result:
                    print(f"You chose {result[1]} : {result[2]}")
                    new_amount = float(input(f"Enter new income amount for {result[1]}: "))
                    cursor.execute("UPDATE tbl_income SET amount = ? WHERE id = ?", (new_amount, income_id))
                    conn.commit()
                    print(f"income '{result[1]}' updated successfully to {new_amount}.")
                else:
                    print("income ID not found. Please enter a valid ID.")
            except Exception as e:
                print(e)
        



# Function to delete an income
def delete_income():
    while True:
        print("You chose the delete option")
        print("Enter ID of income to delete")
        print("Enter num 0 to return to te previous menu")
        view_income()
        income_id = int(input("Enter the ID of the income to delete: "))
        if income_id == 0:
            print("Bye")
            break
        else:
            try:
                cursor.execute("SELECT * FROM tbl_income WHERE id = ?", (income_id,))
                result = cursor.fetchone()
                if result:
                    print(f"you chose {result[1]}")
                    cursor.execute("DELETE FROM tbl_income WHERE id = ?", (income_id,))
                    conn.commit()
                    print(f"income '{result[1]}' deleted")
                else:
                    print("income ID not found. Please enter a valid ID.")
            except Exception as e:
                print(e)
        

