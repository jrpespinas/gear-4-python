from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Find the addends of the list whose sum is equal to the given `target`

    >>> two_sum([2,7,1,6], 9)
    [0, 1]
    """
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        else:
            hashmap[num] = i
