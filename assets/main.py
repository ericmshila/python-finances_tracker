from income import *
from expenses import *

def main():
    while True:
        print("\n MAIN MENU")
        print("\n Welcome to your budget and finances tracker:")
        print("1. Income Menu")
        print("2. Expense Menu")
        print("3. Exit The Program")
    
        choice = input("Choose an option (1-3): ")
    
        if choice == '1':
            income_menu()
        elif choice == '2':
            expense_menu()
        elif choice == '3':
            print("Exiting the program. Goodbye!!!")
            break
        else:
            print("Invalid choice. Please try again.") 


def income_menu():
    while True:
        print("\nincome Tracker Menu:")
        print("1. Add income")
        print("2. View incomes")
        print("3. Edit income")
        print("4. Delete income")
        print("5. Return to main menu")
    
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_income()
        elif choice == '2':
            view_income()
        elif choice == '3':
            edit_income()
        elif choice == '4':
            delete_income()
        elif choice == '5':
            print("Bye!!!")
            break
        else:
            print("Invalid choice. Please try again.")    

def expense_menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Return to main menu")
    
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
            print("Bye!!!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    init_db()
    main()
    close_connection()