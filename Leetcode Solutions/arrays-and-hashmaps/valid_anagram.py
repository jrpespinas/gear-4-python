from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """check for duplicated integers in the list

    >>> contains_duplicate([1,3,5,7,1])
    True
    """
    hashmap = {}
    for i in nums:
        if i in hashmap:
            return True
        else:
            hashmap[i] = 1
    return False
