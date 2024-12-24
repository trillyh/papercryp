from typing import Dict
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



if __name__ == "__main__":
    account = Account("trilly", initial_balance=10000)
    
    account.add_order(order_id=1, asset="BTC", order_type="buy", quantity=0.1, price=30000)
    account.add_order(order_id=2, asset="ETH", order_type="sell", quantity=1.0, price=2000)
    
    print("All Orders:", account.orders)



    