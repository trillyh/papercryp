import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error, IntegrityError

load_dotenv()
class DatabaseUtils:
    def __init__(self):
        self.host = os.getenv("MYSQL_HOST")
        self.port = int(os.getenv("MYSQL_PORT", 3306))
        self.user = os.getenv("MYSQL_USER")
        self.password = os.getenv("MYSQL_PASSWORD")
        self.database = os.getenv("MYSQL_DATABASE")

        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database.")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def create_table(self, table_name: str, schema: str):
        """
        Create a table in the database.

        :param table_name: Name of the table to create.
        :param schema: SQL schema for the table.
        """
        if not self.connection:
            print("Error: No database connection.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})")
            print(f"Table '{table_name}' created or already exists.")
        except Error as e:
            print(f"Error creating table '{table_name}': {e}")
            raise
        finally:
            cursor.close()

    def execute_query(self, query: str, params=None):
        """
        Execute a general SQL query.

        :param query: The SQL query to execute.
        :param params: Parameters for the query (optional).
        """
        if not self.connection:
            print("Error: No database connection.")
            return

        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully.")

        except IntegrityError as e:
            if "FOREIGN KEY" in str(e):
                print("Error: Foreign key constraint failed. Likely, the user_id does not exist in the users table.")
            else:
                print(f"Integrity Error: {e}")
        except Error as e:
            print(f"Error executing query: {e}")
            raise
        finally:
            if cursor:
                cursor.close()

                
    def close(self):
        self.connection.close()
        return True
        
