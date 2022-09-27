import multiprocessing
import time


def count(count_to: int) -> int:
    start = time.time()
    count = 0
    while count < count_to:
        count += 1

    end = time.time()
    print(f"finished counting to {count_to} in {end - start}")
    return count


if __name__ == "__main__":
    start_time = time.time()
    to_one_hundred_million = multiprocessing.Process(target=count, args=(100_000_000,))
    to_two_hundred_million = multiprocessing.Process(target=count, args=(200_000_000,))

    to_one_hundred_million.start()
    to_two_hundred_million.start()
    to_one_hundred_million.join()
    to_two_hundred_million.join()

    end_time = time.time()
    print(f"completed in {end_time - start_time}")
