import uuid
import account
from order import add_order
from utils.db import DatabaseUtils

TEST_USERID = "fc30cd05-bbe2-491e-9b5b-146fd67ac813"

def generate_user_id() -> str:
    return str(uuid.uuid4())

def create_and_insert_users() -> str:
    db = DatabaseUtils()
    db.connect()


    # Create users table
    users_table_name = "users"
    users_schema = """
        id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    """
    db.create_table(users_table_name, users_schema)

    # User data
    user_data = [
        {"name": "Trilly"},
        {"name": "Gold"}
    ]

    for user in user_data:
        if user_exists(db, user["name"]):
            print(f"User '{user['name']}' already exists.")
        else:
            user_id = generate_user_id()
            insert_user_query = """
                INSERT INTO users (id, name) VALUES (%s, %s)
            """
            db.execute_query(insert_user_query, (user_id, user["name"]))
            print(f"User '{user['name']}' added with ID: {user_id}")


def insert_users():
    try:
        db = DatabaseUtils()
        db.connect()


        
        insert_order = """
            INSERT INTO orders (user_id, order_id, asset, order_type, quantity, price, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        order_data = [
            ("", "order1", "BTC", "buy", 0.1, 30000, "open"), 
            ("", "order2", "ETH", "sell", 1.0, 2000, "open")             
        ]

        
        for order in order_data:
            ...
            # db.execute_query(insert_order, order)
    finally:    
        db.close()

def create_orders_table():
    db = DatabaseUtils()
    db.connect()

# Create table
    table_name = "orders"
    orders_schema = """
        id INT AUTO_INCREMENT PRIMARY KEY,
        account_id INT NOT NULL,
        order_id VARCHAR(255) NOT NULL,
        asset VARCHAR(50),
        order_type VARCHAR(50),
        quantity FLOAT,
        price FLOAT,
        status VARCHAR(20),
        FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
    """
    db.create_table(table_name, orders_schema)

    
    

if __name__ == "__main__":
    create_orders_table()

    account1 = account.Account("test_account", initial_balance=1000)
    
    order_id_1 = add_order(account1, asset="BTC", order_type="buy", quantity=0.1, price=30000)
    
    order_id_2 = add_order(account1, asset="ETH", order_type="sell", quantity=1.0, price=2000)
    
    print(f"{account1}")
