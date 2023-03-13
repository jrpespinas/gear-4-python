def is_palindrome(s: str) -> bool:
    """check if the given string is a palindrome

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    """
    s = "".join(char.lower() for char in s if char.isalnum())
    for i in range(len(s) // 2):
        ptr1, ptr2 = s[i], s[len(s) - 1 - i]
        if ptr1 != ptr2:
            return False
    return True


def is_palindrome_2(s: str) -> bool:
    """check if the given string is a palindrome

    >>> is_palindrome_2("A man, a plan, a canal: Panama")
    True
    """
    s = "".join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]


def is_palindrome_3(s: str) -> bool:
    """check if the given string is a palindrome

    >>> is_palindrome_3("A man, a plan, a canal: Panama")
    True
    """
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not is_alnum(s[l]):
            l += 1

        while r > l and not is_alnum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


def is_alnum(s: str) -> bool:
    return "a" <= s.lower() <= "z" or "0" <= s.lower() <= "9"
