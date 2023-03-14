from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """find the index of the target if it exists

    >>> binary_search([-1,0,3,5,9,12], 9)
    4
    >>> binary_search([-1,0,3,5,9,12], 2)
    -1
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1
