import asyncio
from concurrent.futures import ProcessPoolExecutor
from typing import (List, Dict)

import asyncpg

from _postgres_schema_creation_statements import PRODUCT_STATEMENT
from utils import async_timed


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(PRODUCT_STATEMENT)


@async_timed()
async def query_products_concurrently(pool, num_queries):
    queries = [query_product(pool) for _ in range(num_queries)]
    return await asyncio.gather(*queries)


def run_in_new_loop(num_queries: int) -> List[Dict]:
    async def run_queries():
        async with asyncpg.create_pool(host="localhost", port=5432, password="password", database="products") as pool:
            return await query_products_concurrently(pool, num_queries)

    results = [dict(result) for result in asyncio.run(run_queries())]

    return results


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    pool = ProcessPoolExecutor()

    tasks = [loop.run_in_executor(pool, run_in_new_loop, 10000) for _ in range(5)]

    all_results = await asyncio.gather(*tasks)
    total_queries = sum(len(result) for result in all_results)

    print(f"retrieved {total_queries} products from the product database")


if __name__ == "__main__":
    asyncio.run(main())
