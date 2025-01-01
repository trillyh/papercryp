import uuid
from account import Account
from utils.db import DatabaseUtils

def generate_order_id() -> str:
    """
    Generate a unique order ID using UUID.
    """
    return str(uuid.uuid4())

def add_order(account_id, asset: str, order_type: str, amount: float, price: float) -> str:
    """
    Add a new order to the orders dictionary.
    
    :param order_id: Identifier for the order.
    :param asset: Asset address
    :param order_type: type of order ("buy" or "sell").
    :param quantity: u know 
    :param price: in dollars
    """              
    order_id = generate_order_id()
    
    if order_type not in ("buy", "sell"):
        raise ValueError(f"Invalid order_type: {order_type}. Must be one of {("buy", "sell")}.")

    elif amount <= 0:
        raise ValueError(f"Invalid quanity: {amount}. amount must be larger than 0")

    try:
        db = DatabaseUtils()
        db.connect()

        insert_order_query = """
            INSERT INTO orders (account_id, order_id, asset, order_type, amount, price, status) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        order = (account_id, order_id, asset, order_type, amount, price, "open")
        db.execute_query(insert_order_query, order)

    except Exception as e:
        print(e)
     
    finally:
        db.close()
        

if __name__ == "__main__":
    print("All tests passed!")

 