import account
from order import add_order


if __name__ == "__main__":
    account1 = account.Account("test_account", initial_balance=1000)
    
    order_id_1 = add_order(account1, asset="BTC", order_type="buy", quantity=0.1, price=30000)
    
    order_id_2 = add_order(account1, asset="ETH", order_type="sell", quantity=1.0, price=2000)
    
    print(f"{account1}")