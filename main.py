import uuid
from utils.db import DatabaseUtils


def generate_user_id() -> str:
    return str(uuid.uuid4())

def user_exists(db: DatabaseUtils, name: str) -> bool:
    """
    Check if a user with the given name exists in the `users` table.

    :param db: DatabaseUtils instance.
    :param name: The name of the user to check.
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
        

def test_create_user() -> str:
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




def create_orders_table():
    db = DatabaseUtils()
    db.connect()

# Create table
    table_name = "orders"
    orders_schema = """
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id VARCHAR(36) NOT NULL,
        order_id VARCHAR(255) NOT NULL,
        asset VARCHAR(50),
        order_type VARCHAR(50),
        quantity FLOAT,
        price FLOAT,
        status VARCHAR(20),
        FOREIGN KEY (user_id) REFERENCES users(id)
    """
    db.create_table(table_name, orders_schema)

# just for testing now
if __name__ == "__main__":
    # CREATE TABLES
    # test_create_user()
    create_orders_table()

    
    #Test
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
        db.execute_query(insert_order, order)


    