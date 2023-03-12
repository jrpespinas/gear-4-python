from collections import defaultdict


def valid_anagram_solution_1(s: str, t: str) -> bool:
    """check if the given strings are each other's anagram

    >>> valid_anagram_solution_1("anagram", "namagra")
    True
    >>> valid_anagram_solution_1("hello", "world")
    False
    """
    if len(s) != len(t):
        return False

    hashS, hashT = {}, {}
    for i in range(len(s)):
        hashS[s[i]] = 1 + hashS.get(s[i], 0)
        hashT[t[i]] = 1 + hashT.get(t[i], 0)

    for i in s:
        if hashS[i] != hashT.get(i, 0):
            return False

    return True


def valid_anagram_solution_2(s: str, t: str) -> bool:
    """check if the given strings are each other's anagram

    >>> valid_anagram_solution_2("anagram", "namagra")
    True
    >>> valid_anagram_solution_2("hello", "world")
    False
    """
    hashS, hashT = defaultdict(int), defaultdict(int)

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        hashS[s[i]] += 1
        hashT[t[i]] += 1

    for i in s:
        if hashS[i] != hashT.get(i, 0):
            return False

    return True
