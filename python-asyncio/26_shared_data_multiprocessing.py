import asyncio
import functools
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Value
from typing import List, DefaultDict

map_progress: Value


def reduce_dictionaries(first: DefaultDict[str, int], second: DefaultDict[str, int]):
    for key in second:
        first[key] += second[key]

    return first


def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i: i + chunk_size]


def init(progress: Value):
    global map_progress
    map_progress = progress


def map_frequencies(chunk: List[str]) -> DefaultDict[str, int]:
    counter = defaultdict(int)
    for line in chunk:
        word, _, count, _ = line.split("\t")
        counter[word] += int(count)

    with map_progress.get_lock():
        map_progress.value += 1

    return counter


async def progress_reporter(total_partitions: int):
    while map_progress.value < total_partitions:
        print(f"finished {map_progress.value}/{total_partitions} map operations")
        await asyncio.sleep(1)


async def main(partition_size: int):
    global map_progress
    with open("/Users/vitalim/Downloads/googlebooks-eng-all-1gram-20120701-a", encoding="utf-8") as input_stream:
        contents = input_stream.readlines()
        loop = asyncio.get_running_loop()
        tasks = list()
        map_progress = Value("i", 0)
        with ProcessPoolExecutor(initializer=init, initargs=(map_progress,)) as pool:
            total_partitions = len(contents) // partition_size
            reporter = asyncio.create_task(progress_reporter(total_partitions))

            for chunk in partition(contents, partition_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

            counters = await asyncio.gather(*tasks)
            await reporter
            final_result = functools.reduce(reduce_dictionaries, counters)
            print(f"Aardvark has appeared {final_result['Aardvark']} times")


if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))
