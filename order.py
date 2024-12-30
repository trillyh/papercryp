import uuid
from account import Account
from utils.db import DatabaseUtils

def generate_order_id() -> str:
    """
    Generate a unique order ID using UUID.
    """
    return str(uuid.uuid4())

def add_order(account_id, asset: str, order_type: str, quantity: float, price: float) -> str:
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

    elif quantity <= 0:
        raise ValueError(f"Invalid quanity: {quantity}. Quantity must be larger than 0")

    try:
        db = DatabaseUtils
        db.connect()

        insert_order_query = """
            INSERT INTO orders (account_id, order_id, asset, order_type, quantity, price, status) VALUES (%s, %s, %s)
        """

        order = (account_id, order_id, order_type, quantity, price, "open")
        db.execute_query(insert_order_query, order)

    except Exception as e:
        print(e)
     
    finally:
        db.close()
        



# TEST FUNCTIONS - not using:w
def test_generate_order_id():
    """
    Test to ensure order IDs are unique.
    """
    id1 = generate_order_id()
    id2 = generate_order_id()
    assert id1 != id2, "Order IDs should be unique."
    print("test_generate_order_id passed.")

def test_add_order():
    """
    Test to ensure orders are correctly added to the account.
    """
    account = Account("test_account", initial_balance=1000)
    
    order_id_1 = add_order(account, asset="BTC", order_type="buy", quantity=0.1, price=30000)
    assert order_id_1 in account.orders, "Order ID 1 should exist in account orders."
    assert account.orders[order_id_1]["asset"] == "BTC", "Order asset should be BTC."
    
    order_id_2 = add_order(account, asset="ETH", order_type="sell", quantity=1.0, price=2000)
    assert order_id_2 in account.orders, "Order ID 2 should exist in account orders."
    assert account.orders[order_id_2]["type"] == "sell", "Order type should be 'sell'."
    
    assert len(account.orders) == 2, "There should be 2 orders in the account."
    print("test_add_order passed.")

if __name__ == "__main__":
    test_generate_order_id()
    test_add_order()
    print("All tests passed!")

 