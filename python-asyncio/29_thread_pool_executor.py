import time
import requests
from concurrent.futures import ThreadPoolExecutor


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


if __name__ == "__main__":
    start = time.perf_counter()
    with ThreadPoolExecutor() as pool:
        urls = ["https://example.com" for _ in range(10)]
        results = pool.map(get_status_code, urls)
        for result in results:
            print(result)

    end = time.perf_counter()
    print(f"finished requests in {end - start:.4f} second(s)")
