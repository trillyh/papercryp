import asyncio
from account import Account
from utils.db import AsyncDatabaseUtils
from order import add_order

account: Account = None

def get_user_input(prompt: str) -> str:
    return input(prompt)

async def main():
    global account
    db = await init_db_pool()

    try:
        while True:
            if account:
                await show_dashboard(db)
                continue

            print("\n--- Main Menu ---")
            print("1. Login")
            print("2. Create User")
            print("3. Quit")

            choice = get_user_input("Enter your choice (1/2/3): ")

            if choice == "1":
                await login_user(db)
            elif choice == "2":
                await create_user(db)
            elif choice == "3":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    finally:
        await close_db_pool(db)


async def login_user(db: AsyncDatabaseUtils):
    global account
    while True:
        account_id = get_user_input("Enter account's id: ")
        account = await Account.get_account(db, account_hash=account_id)
        if account:
            print(f"Logged in! Welcome {account.name}")
            break
        else:
            print("User not found. Please create an account first.")


async def create_user(db: AsyncDatabaseUtils):
    global account
    while True:
        name = get_user_input("Enter username: ")
        try:
            initial_balance = float(get_user_input("Enter initial balance: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for the initial balance.")
            continue

        account = await Account.create_account(db, name, initial_balance)
        if account:
            print(f"Created and logged in! Welcome {name}")
            break


async def show_dashboard(db: AsyncDatabaseUtils):
    global account

    print("\n--- User Dashboard ---")
    print(f"Welcome, {account.name}!")
    print(f"Current Balance: ${account.solana_balance:.5f}")
    print("\nTo log out, type 'logout'. To quit, type 'quit'.")
    print("Enter any command, separated by space")

    user_input = get_user_input("Enter your choice: ").strip().lower().split()
    
    command = user_input[0] if user_input else ""

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
            return

        try:
            price = float(user_input[3])
        except ValueError:
            print("Invalid input. Please enter a valid number for price.")
            return

        await add_order(db, account_id=account.account_id, order_type="buy", asset=asset_address, amount=amount, price=price)
        print("Order added successfully.")

    elif command == "sell":
        print("sell")


async def init_db_pool() -> AsyncDatabaseUtils:
    db = AsyncDatabaseUtils()
    await db.connect()
    return db


async def close_db_pool(db: AsyncDatabaseUtils):
    await db.close()


if __name__ == "__main__":
    asyncio.run(main())
