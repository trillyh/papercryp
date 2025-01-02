import asyncio
import aiomysql
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("utils/.env") #change env loc
load_dotenv(dotenv_path=dotenv_path)

host = os.getenv("MYSQL_HOST")
port = int(os.getenv("MYSQL_PORT", 3306))
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")


loop = asyncio.get_event_loop()

async def test_example():
    conn = await aiomysql.connect(host=host, port=port,
                                  user=user, password=password, db=database,
                                  loop=loop)

    cur = await conn.cursor()
    await cur.execute("SELECT account_id FROM accounts")
    print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()

loop.run_until_complete(test_example())