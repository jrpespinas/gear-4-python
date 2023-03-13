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
