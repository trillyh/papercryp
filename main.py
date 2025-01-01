import uuid
from utils.db import DatabaseUtils
import test
from account import Account
from order import add_order
account: Account = None
def main():
    global account
    while True:
        if account:
            show_dashboard() 
            continue
        
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
    """
    Use user's id to login 
    """
    global account
    while True:
        account_id= input("Enter account's id: ")
        account = Account.get_account(account_hash=account_id)
        if account:
            print(f"Created and logged in! Welcome {account.name}")
            break
        else:
            print(f"User not found. Please create an account first.")   
             
        
def create_user():
    global account
    while True: 
        name = input("Enter username: ")
        initial_balance = float(input("Enter initial balance: "))
        account = Account.create_account(name, initial_balance)
        if account:
            print(f"Created and logged in! Welcome {name}")
            break

def show_dashboard():
    """Show the dashboard once logged in"""

    global account

    print("\n--- User Dashboard ---")
    print(f"Welcome, {account.name}!")
    print(f"Current Balance: ${account.solana_balance:.5f}")
    print("\nTo log out, type 'logout'. To quit, type 'quit'.")
    print("Enter any command, separate by space")
    
    user_input = input("Enter your choice: ").strip().lower()
    user_input = user_input.split() 

    command = user_input[0]
    
    if command == "logout":
        account = None
        print("You have been logged out.")
    elif command == "quit":
        print("Exiting the program. Goodbye!")
        exit()

    elif command == "buy":
        if len(user_input) != 4:
            print("Enter in the form: buy (asset_address) (amount) (price)")
            return

        asset_address = user_input[1]

        try:
            amount = float(user_input[2])
        except ValueError:
            print("Invalid input. Please enter a valid number for amount.")

        price = user_input[3]

        add_order(account_id= account.account_id,
                    order_type="buy",
                    asset=asset_address, 
                    amount=amount, 
                    price=price)

        print("added order")
    
            

    elif command == "sell":
        print("sell")
    
    

# just for testing now
if __name__ == "__main__": 
    main()
   