from db import DatabaseUtils

"""
This file necessary tables for the programs
"""
def create_accounts_table():

    accounts_schema = """
        account_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        account_address VARCHAR(255) UNIQUE,
        balance DECIMAL(15, 2) DEFAULT 0.00
    """
    db = DatabaseUtils()
    try:
        db.connect()
        db.create_table("accounts", accounts_schema)
        print("`accounts` table created successfully.")
    except Exception as e:
        print(f"Error creating `accounts` table: {e}")
    finally:
        db.close()


def create_orders_table():
    """
    Create the `orders` table.
    """
    orders_schema = """
        id INT AUTO_INCREMENT PRIMARY KEY,
        account_id INT NOT NULL,
        order_id VARCHAR(255) NOT NULL UNIQUE,
        asset VARCHAR(50),
        order_type VARCHAR(50),
        amount FLOAT,
        price FLOAT,
        status VARCHAR(20),
        FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
    """
    db = DatabaseUtils()
    try:
        db.connect()
        db.create_table("orders", orders_schema)
        print("`orders` table created successfully.")
    except Exception as e:
        print(f"Error creating `orders` table: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    create_accounts_table()
    create_orders_table()
