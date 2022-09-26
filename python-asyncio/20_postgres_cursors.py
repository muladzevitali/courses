import asyncio

from utils import get_postgres_connection


async def main():
    connection = await get_postgres_connection()
    query = "select product_id, product_name from product"

    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)

    await connection.close()


async def move_cursor():
    connection = await get_postgres_connection()

    query = "select product_id, product_name from product"

    async with connection.transaction():
        cursor = await connection.cursor(query)
        await cursor.forward(500)

        products = await cursor.fetch(100)
        for product in products:
            print(product)

    await connection.close()


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return

        item_count += 1
        yield item


if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(move_cursor())
