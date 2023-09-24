import bisect
from typing import List


def find(array: List[int], number):
    left = 0
    right = len(array) - 1

    while left <= right:
        index = (left + right) // 2

        if array[index] > number:
            right = index - 1
        elif array[index] < number:
            left = index + 1
        else:
            return index

    return None


def find_recursive(array: List[int], number: int, left: int = None, right: int = None):
    left, right = left if left is not None else 0, right if right is not None else len(array) - 1

    if left > right:
        return

    middle = (left + right) // 2

    if array[middle] > number:
        return find_recursive(array, number, left, middle - 1)

    if array[middle] < number:
        return find_recursive(array, number, middle + 1, right)

    return middle


def find_bisect(array: List[int], number: int):
    index = bisect.bisect_left(array, number)

    if index == len(array):
        return

    return index if array[index] == number else None


def test_find_function(search_function):
    a = [1, 2, 3, 4, 5, 6, 7]
    search_index = search_function(a, 3)
    assert search_index == 2, "invalid result"
    print(search_index)

    search_index = search_function(a, 10)
    assert search_index is None, "invalid result"
    print(search_index)

    assert search_function(a, -1) is None, "invalid result"


if __name__ == "__main__":
    test_find_function(find_bisect)
