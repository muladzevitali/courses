import asyncio
import logging

import asyncpg
from asyncpg.transaction import Transaction

from utils import get_postgres_connection


async def main():
    connection = await asyncpg.connect(host="localhost", port=5432, database="products", password="password")

    async with connection.transaction():
        await connection.execute("insert into brand values(default, 'brand_1')")
        await connection.execute("insert into brand values(default, 'brand_2')")
    query = """select brand_name from brand where brand_name like 'brand%'"""

    brands = await connection.fetch(query)
    print(brands)
    await connection.close()


async def main_with_error():
    connection = await asyncpg.connect(host="localhost", port=5432, database="products", password="password")
    try:
        async with connection.transaction():
            insert_brand = "insert into brand value(999, 'big_brand')"
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception:
        logging.exception("error while running transaction")
    finally:
        query = """select brand_name from brand where brand_name like 'big_%'"""
        brands = await connection.fetch(query)
        print(f"query result was: {brands}")

        await connection.close()


async def main_with_save_points():
    connection = await asyncpg.connect(host="localhost", port=5432, database="products", password="password")
    async with connection.transaction():
        await connection.execute("insert into brand values(default, 'my_new_brand')")
        try:
            async with connection.transaction():
                await connection.execute("insert into product_color values(1, 'black')")
        except Exception as ex:
            logging.exception("ignoring error inserting product color", exc_info=ex)

    await connection.close()


async def manual_rollback():
    connection = await get_postgres_connection()
    transaction: Transaction = connection.transaction()
    await transaction.start()
    try:
        await connection.execute("insert into brand values (default, 'brand_1')")
        await connection.execute("insert into brand values (1, 'brand_2')")
    except asyncpg.PostgresError:
        print("errors, rolling back the transaction")
        await transaction.rollback()
    else:
        print("no errors, committing the transaction")
        await transaction.commit()

    query = """select brand_name from brand where brand_name like 'brand_%'"""
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


if __name__ == "__main__":
    # asyncio.run(main_with_error())
    # asyncio.run(main_with_save_points())
    asyncio.run(manual_rollback())
