from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """check for duplicated integers in the list

    >>> contains_duplicate([1,3,5,7,1])
    True
    >>> contains_duplicate([1,2,3,4,5])
    False
    """
    hashmap = {}
    for i in nums:
        if i in hashmap:
            return True
        else:
            hashmap[i] = 1
    return False
