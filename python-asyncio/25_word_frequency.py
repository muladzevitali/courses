import asyncio
import concurrent
import functools
import time
from collections import defaultdict
from typing import (List, DefaultDict)


def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i: i + chunk_size]


def map_frequencies(chunk: List[str]) -> DefaultDict[str, int]:
    counter = defaultdict(int)
    for line in chunk:
        word, _, count, _ = line.split("\t")
        counter[word] += int(count)

    return counter


def reduce_dictionaries(first: DefaultDict[str, int], second: DefaultDict[str, int]):
    for key in second:
        first[key] += second[key]

    return first


async def reduce_dictionaries_async(loop, pool, counters, chunk_size) -> DefaultDict[str, int]:
    chunks: List[List[DefaultDict]] = list(partition(counters, chunk_size))
    reducers = list()

    while len(chunks[0]) > 1:
        for chunk in chunks:
            reducer = functools.partial(functools.reduce, reduce_dictionaries, chunk)
            reducers.append(loop.run_in_executor(pool, reducer))

        reducer_chunks = await asyncio.gather(*reducers)
        chunks = list(partition(reducer_chunks, chunk_size))
        reducers.clear()

    return chunks[0][0]


async def main(partition_size):
    with open("/Users/vitalim/Downloads/googlebooks-eng-all-1gram-20120701-a", encoding="utf-8") as input_stream:
        contents = input_stream.readlines()

        loop = asyncio.get_running_loop()
        tasks = list()
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            for chunk in partition(contents, partition_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))
            intermediate_results = await asyncio.gather(*tasks)
            final_results = await reduce_dictionaries_async(loop, pool, intermediate_results, 500)

            print(f"Aardvark has appeared {final_results['Aardvark']} times")
            end = time.time()
            print(f"mapreduce took: {end - start:.4f} seconds")


if __name__ == "__main__":
    asyncio.run(main(partition_size=60_000))
