import uuid
from utils.db import DatabaseUtils
import test
from account import Account

account: Account = None
def main():
     while True:
        if account:
            ... # show dashboard
        
        print("\n--- Main Menu ---")
        print("1. Login")
        print("2. Create User")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            login_user()
        elif choice == "2":
            create_user()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.") 

def login_user():
    ...

def create_user():
    name = input("Enter username: ")
    initial_balance = float(input("Enter initial balance: "))
    Account.create_user(name, initial_balance)
    print()
    

# just for testing now
if __name__ == "__main__": 
    main()
   