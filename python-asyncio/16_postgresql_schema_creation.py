import asyncio
from random import (sample, randint)
from typing import (List, Tuple, Union)

import asyncpg

from _postgres_schema_creation_statements import *


async def main():
    connection = await asyncpg.connect(host="localhost", port="5432", database="products", password="password")
    statements = (CREATE_BRAND_TABLE, CREATE_PRODUCT_TABLE, CREATE_PRODUCT_COLOR_TABLE, CREATE_PRODUCT_SIZE_TABLE,
                  CREATE_SKU_TABLE, SIZE_INSERT, COLOR_INSERT)
    print("creating the product database ...")
    for statement in statements:
        status = await connection.execute(statement)
        print(status)

    print("finished creating the product database")
    await connection.close()


async def insert_data():
    common_words = load_common_words()

    connection = await asyncpg.connect(host="localhost", port="5432", database="products", password="password")
    await insert_brands(common_words, connection)

    brand_query = 'select brand_id, brand_name from brand'
    results: List[asyncpg.Record] = await connection.fetch(brand_query)
    for brand in results[:10]:
        print(f"id: {brand['brand_id']}, name: {brand['brand_name']}")

    await connection.close()


def load_common_words() -> List[str]:
    with open("common_words.txt") as input_stream:
        return input_stream.readlines()


def generate_brand_names(words: List[str]) -> List[Tuple[Union[str,]]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands_statement = 'insert into brand values (default, $1)'

    return await connection.executemany(insert_brands_statement, brands)


def generate_products(common_words: List[str], brand_id_start: int,
                      brand_id_end: int, products_to_create: int) -> List[Tuple[str, int]]:
    products = list()
    for _ in range(products_to_create):
        description = [common_words[index] for index in sample(range(1000), 10)]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((" ".join(description), brand_id))

    return products


def generate_sku(product_id_start: int, product_id_end: int, skus_to_create: int) -> List[Tuple[int, int, int]]:
    skus = list()

    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))

    return skus


async def insert_products():
    common_words = load_common_words()
    connection = await asyncpg.connect(host="localhost", port=5432, database="products", password="password")

    product_tuples = generate_products(common_words, brand_id_start=1, brand_id_end=100, products_to_create=1000)
    await connection.executemany('insert into product values(default, $1, $2)', product_tuples)

    sku_tuples = generate_sku(product_id_start=1, product_id_end=1000, skus_to_create=100000)
    await connection.executemany('insert into sku values (default, $1, $2, $3)', sku_tuples)

    await connection.close()


async def fetch_test_row():
    product_statement = """
    select
    p.product_id, p.product_name, p.brand_id, s.sku_id, pc.product_color_name, ps.product_size_name
    from product p 
    join sku s on s.product_id=p.product_id
    join product_color pc on pc.product_color_id=s.product_color
    join product_size ps on ps.product_size_id=s.product_size_id
    
    where p.product_id=100
    """

    connection = await asyncpg.connect(host="localhost", port=5432, database="products", password="password")
    queries = (connection.execute(product_statement), )

    results = await asyncio.gather(*queries)
    print(results)


if __name__ == "__main__":
    # asyncio.run(main())
    # asyncio.run(insert_data())
    # asyncio.run(insert_products())
    asyncio.run(fetch_test_row())