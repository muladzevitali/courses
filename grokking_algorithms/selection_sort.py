import timeit
from typing import List


def find_smallest(array: List[int]):
    return min(range(len(array)), key=lambda x: array[x])


def find_smallest_element_index(array: List[int]):
    return array.index(min(array))


def selection_sort(array: List[int]):
    sorted_array: List[int] = list()

    for index in range(len(array)):
        smallest_element_index = find_smallest(array)
        sorted_array.append(array.pop(smallest_element_index))

    return sorted_array


if __name__ == "__main__":
    print(selection_sort([3, 2, 1, 0, -1]))

    print(timeit.timeit("find_smallest(list(range(1_000_000)))", number=100, globals=globals()))
    print(timeit.timeit("find_smallest_element_index(list(range(1_000_000)))", number=100, globals=globals()))
