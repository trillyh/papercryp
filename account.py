from typing import Dict, Optional
import uuid
from utils.db import DatabaseUtils



class Account:
    def __init__(self, name, initial_balance=0.0):
        """
        Fields of an account:  
        """
        self.name = name
        self.solana_balance = initial_balance  # Cash balance in the account
        self.dollar_balance = 0 # sol * USD price
        self.net_worth = 0 # USD balance + holding
        self.holdings: Dict[str, float] = {}
        self.orders: Dict = {} 
        self.transaction_history = {}

    @classmethod    
    def user_exists(cls, db: DatabaseUtils, name: str) -> bool:
        """
        Check if a user with the given name exists in the `users` table.

        :param db: DatabaseUtils instance.
        :param name: name to check
        :return: True if the user exists, False otherwise.
        """
        query = "SELECT COUNT(*) FROM users WHERE name = %s"
        try:
            conn = db.connection
            cursor = conn.cursor()
            cursor.execute(query, (name,))
            count = cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print(f"Error checking if user exists: {e}")
            return False
        finally:
            cursor.close()

    @classmethod        
    def create_user(cls, name, initial_balance) -> Optional["Account"]:
        """
        Create a user account. 
        :param name: The name of the user to check.
        :param initial_balance: init balance.
        :return: None if acount already exist, Account instance otherwise.
        """
        try:
            db = DatabaseUtils()
            db.connect()
        
            if cls.user_exists(db, name):
                print("Create user error: User already exist")
                return None
            try: 
                user_id = str(uuid.uuid4())
                insert_user_query = """
                    INSERT INTO users (id, name) VALUES (%s, %s)
                """
                db.execute_query(insert_user_query, (user_id, name))

            except Exception as e:
                print(f"Error while creating user {e}")
                return None
            return cls(name, initial_balance)

        finally: 
            db.close()
             
    def add_order(self, new_order: Dict):
        """
        Add a new order to the orders dictionary.
        
        :param order_id: Identifier for the order.
        :param asset: Asset address
        :param order_type: type of order ("buy" or "sell").
        :param quantity: u know 
        :param price: in dollars
        """        
        order_id = new_order["order_id"]
        self.orders[order_id] = new_order
        print(f"Added new order: {self.orders[order_id]}")

    def add_account_transaction(self, order: Dict):
        pass
    
    def set_account_balance(self, order: Dict):
        pass

    def recalculate_account_networth(self, order: Dict):
        pass

    def create_table(self):
        """
        Create tables for account
        """
        self.db_connection = sqlite3.connect("accounts.db")
        self.create_table()
        cursor = self.db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                solana_balance REAL,
                dollar_balance REAL,
                net_worth REAL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_name TEXT,
                order_id TEXT,
                asset TEXT,
                order_type TEXT,
                quantity REAL,
                price REAL,
                status TEXT,
                FOREIGN KEY (account_name) REFERENCES accounts (name)
            )
        """)


if __name__ == "__main__":
    account = Account("trilly", initial_balance=10000)
    
#    account.add_order(order_id=1, asset="BTC", order_type="buy", quantity=0.1, price=30000)
#    account.add_order(order_id=2, asset="ETH", order_type="sell", quantity=1.0, price=2000)
    
    print("All Orders:", account.orders)



    
