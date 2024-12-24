import uuid
import account

def generate_order_id() -> str:
    return str(uuid.uuid4())


def add_order(account: account.Account, asset: str, order_type: str, quantity: float, price: float):
    """
    Add a new order to the orders dictionary.
    
    :param order_id: Identifier for the order.
    :param asset: Asset address
    :param order_type: type of order ("buy" or "sell").
    :param quantity: u know 
    :param price: in dollars
    """        

    order_id = generate_order_id()
    new_order = {
        "order_id": order_id, 
        "asset": asset,
        "type": order_type,
        "quantity": quantity,
        "price": price,
        "status": "open" 
    }
    account.add_orders(new_order)
    print(f"Added new order: {[order_id]}")














# TEST FUNCTIONS
def test_generate_order_id():
    id1 = generate_order_id()
    id2 = generate_order_id()
    assert id1 != id2, "Order IDs should be unique."
    print("test_generate_order_id passed.")

def test_add_order():
    account = account.Account("test_account", initial_balance=1000)
    
    # Add a buy order
    order_id_1 = add_order(account, asset="BTC", order_type="buy", quantity=0.1, price=30000)
    assert order_id_1 in account.orders, "Order ID 1 should exist in account orders."
    assert account.orders[order_id_1]["asset"] == "BTC", "Order asset should be BTC."
    
    # Add a sell order
    order_id_2 = add_order(account, asset="ETH", order_type="sell", quantity=1.0, price=2000)
    assert order_id_2 in account.orders, "Order ID 2 should exist in account orders."
    assert account.orders[order_id_2]["type"] == "sell", "Order type should be 'sell'."
    
    # Ensure both orders are added
    assert len(account.orders) == 2, "There should be 2 orders in the account."
    print("test_add_order passed.")

if __name__ == "__main__":
    # Run tests
    test_generate_order_id()
    test_add_order()
    print("All tests passed!")


 