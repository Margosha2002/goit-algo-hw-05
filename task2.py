from random import randint

T = tuple[int, any]


def get_list(size: int):
    return list(sorted([randint(1, 50) for _ in range(size)]))


def binary_search(iterable: list[any], target: any):
    left, right = 0, len(iterable) - 1
    iterations = 0

    if target >= iterable[right]:
        return 0, iterable[right]
    if target <= iterable[left]:
        return 0, iterable[left]

    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1

        if iterable[mid] < target:
            left = mid + 1
        elif iterable[mid] >= target:
            right = mid - 1

    return iterations, iterable[left]


if __name__ == "__main__":
    print(array := get_list(30))
    print(target := randint(1, 50))
    print(binary_search(iterable=array, target=target))
