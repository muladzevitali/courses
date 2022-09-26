import asyncio

import asyncpg

from _postgres_schema_creation_statements import PRODUCT_STATEMENT
from utils import async_timed


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(PRODUCT_STATEMENT)


@async_timed()
async def query_products_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timed()
async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    await asyncio.gather(*queries)


async def main():
    async with asyncpg.create_pool(host="localhost", port=5432, database='products', password="password",
                                   min_size=6, max_size=6) as pool:
        await query_products_synchronously(pool, 10000)
        await query_products_concurrently(pool, 10000)


if __name__ == "__main__":
    asyncio.run(main())
