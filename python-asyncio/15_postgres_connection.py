import asyncio

import asyncpg


async def main():
    connection = await asyncpg.connect(host="localhost", port=5432, database="postgres", password="password")
    version = connection.get_server_version()
    print(f"connected to postgres version {version}")
    await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
