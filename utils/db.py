import os
import asyncio
from dotenv import load_dotenv
import aiomysql

load_dotenv()

class AsyncDatabaseUtils:
    def __init__(self):
        self.host = os.getenv("MYSQL_HOST")
        self.port = int(os.getenv("MYSQL_PORT", 3306))
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database = os.getenv("MYSQL_DATABASE")

        self.pool = None

    async def connect(self):
        try:
            self.pool = await aiomysql.create_pool(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.database,
                minsize=1,
                maxsize=10
            )
            print("Connected to MySQL database.")
        except Exception as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    async def create_table(self, table_name: str, schema: str):
        """
        Create a table in the database.

        :param table_name: Name of the table to create.
        :param schema: SQL schema for the table.
        """
        if not self.pool:
            print("Error: No database connection.")
            return

        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                try:
                    await cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})")
                    print(f"Table '{table_name}' created or already exists.")
                except Exception as e:
                    print(f"Error creating table '{table_name}': {e}")
                    raise

    async def execute_query(self, query: str, params=None):
        """
        Execute a general SQL query.

        :param query: The SQL query to execute.
        :param params: Parameters for the query (optional).
        """
        if not self.pool:
            print("Error: No database connection.")
            return

        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                try:
                    await cursor.execute(query, params)
                    await conn.commit()
                    print("Query executed successfully.")
                except Exception as e:
                    print(f"Error executing query: {e}")
                    raise

    async def close(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()
            print("Connection pool closed.")
        
