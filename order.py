import uuid

def generate_order_id() -> str:
    return str(uuid.uuid4())


def add_order(self, asset: str, order_type: str, quantity: float, price: float):
    """
    Add a new order to the orders dictionary.
    
    :param order_id: Identifier for the order.
    :param asset: Asset address
    :param order_type: type of order ("buy" or "sell").
    :param quantity: u know 
    :param price: in dollars
    """        

    order_id = self.generate_order_id()
    self.orders[order_id] = {
        "asset": asset,
        "type": order_type,
        "quantity": quantity,
        "price": price,
        "status": "open" 
    }
    print(f"Added new order: {self.orders[order_id]}")

 