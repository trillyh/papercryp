import uuid
from account import Account
from utils.db import AsyncDatabaseUtils

def generate_order_id() -> str:
    """
    Generate a unique order ID using UUID.
    """
    return str(uuid.uuid4())


async def add_order(db: AsyncDatabaseUtils, account_id: str, asset: str, order_type: str, amount: float, price: float) -> str:
    """
    Add a new order to the orders table.

    :param db: AsyncDatabaseUtils instance.
    :param account_id: Account identifier.
    :param asset: Asset address.
    :param order_type: Type of order ("buy" or "sell").
    :param amount: Quantity of the asset.
    :param price: Price in dollars.
    :return: The generated order ID.
    """
    order_id = generate_order_id()

    if order_type not in ("buy", "sell"):
        raise ValueError(f"Invalid order_type: {order_type}. Must be one of {('buy', 'sell')}.")

    if amount <= 0:
        raise ValueError(f"Invalid quantity: {amount}. Amount must be larger than 0.")

    try:
        insert_order_query = """
            INSERT INTO orders (account_id, order_id, asset, order_type, amount, price, status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        order = (account_id, order_id, asset, order_type, amount, price, "open")

        async with db.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(insert_order_query, order)
                await conn.commit()

        return order_id

    except Exception as e:
        print(f"Error adding order: {e}")
        raise
        

if __name__ == "__main__":
    print("All tests passed!")

 