import asyncio
import aiomysql
import os
from dotenv import load_dotenv
from pathlib import Path
from utils.db import AsyncDatabaseUtils




async def check_market():
    dotenv_path = Path("utils/.env") #change env loc
    load_dotenv(dotenv_path=dotenv_path)

    host = os.getenv("MYSQL_HOST") 
    assert host is not None, "Can't find Host env"
    port = int(os.getenv("MYSQL_PORT", 3306))
    user = os.getenv("MYSQL_USER")
    password = os.getenv("MYSQL_PASSWORD")
    database = os.getenv("MYSQL_DATABASE")



    cur = await conn.cursor()
    await cur.execute("SELECT account_id FROM accounts")
    print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()

loop.run_until_complete(test_example())




async def init_db_pool() -> AsyncDatabaseUtils:
    db = AsyncDatabaseUtils()
    await db.connect()
    return db


async def close_db_pool(db: AsyncDatabaseUtils):
    await db.close()


if __name__ == "__main__":
    asyncio.run(main())

