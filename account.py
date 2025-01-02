from typing import Dict, Optional
import uuid
from utils.db import AsyncDatabaseUtils


class Account:
    def __init__(self, name, initial_balance=0.0):
        """
        Fields of an account:  
        """
        self.name = name
        self.account_id = None
        self.solana_balance = initial_balance  # Cash balance in the account
        self.dollar_balance = 0 # sol * USD price
        self.net_worth = 0 # USD balance + holding
        self.holdings: Dict[str, float] = {}
        self.orders: Dict = {} 
        self.transaction_history = {}

    @classmethod    
    async def user_exists(cls, db: AsyncDatabaseUtils, name: str) -> bool:
        """
        Check if a user with the given name exists in the 'users' table.

        :param db: AsyncDatabaseUtils instance.
        :param name: name to check
        :return: True if the user exists, False otherwise.
        """
        query = "SELECT COUNT(*) FROM accounts WHERE name = %s"
        try:
            async with db.pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute(query, (name,))
                    count = (await cursor.fetchone())[0]
                    return count > 0
        except Exception as e:
            print(f"Error checking if user exists: {e}")
            return False

    @classmethod
    async def get_account(cls, db: AsyncDatabaseUtils, account_hash: str) -> Optional["Account"]:
        """
        Get the account information from db, also set the account_id
        
        :param cls
        :account_id: account_id
        """
        query = "SELECT account_id, name, balance FROM accounts WHERE account_address = %s"
        try:
            async with db.pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    await cursor.execute(query, (account_hash,))
                    user = await cursor.fetchone()
                    if user: 
                        account = cls(user[1], user[2])
                        account.account_id = user[0]
                        return account
        except Exception as e:
            print(f"Error during login: {e}")
        
    @classmethod        
    async def create_account(cls, db: AsyncDatabaseUtils, name, initial_balance) -> Optional["Account"]:
        """
        Create a user account. 
        :param name: The name of the user to check.
        :param initial_balance: init balance.
        :return: None if account already exists, Account instance otherwise.
        """
        try:
            if await cls.user_exists(db, name):
                print("Create user error: User already exists")
                return None
            try: 
                user_id = str(uuid.uuid4())
                insert_user_query = """
                    INSERT INTO accounts (account_address, name, balance) VALUES (%s, %s, %s)
                """
                async with db.pool.acquire() as conn:
                    async with conn.cursor() as cursor:
                        await cursor.execute(insert_user_query, (user_id, name, initial_balance))
                        await conn.commit()
            except Exception as e:
                print(f"Error while creating user {e}")
                return None
            return cls(name, initial_balance)
        
        except Exception as e:
            print(f"Error in create_account: {e}")

    def add_account_transaction(self, order: Dict):
        pass
    
    def set_account_balance(self, order: Dict):
        pass

    def recalculate_account_networth(self, order: Dict):
        pass

    
