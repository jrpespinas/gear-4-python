def isPalindrome(s: str) -> bool:
    """check if the given string is a palindrome

    >>> isPalindrome("A man, a plan, a canal: Panama")
    True
    """
    s = s.replace(" ", "")
    s = s.lower()
    s = "".join(char for char in s if char.isalpha())
    for i in range(len(s) // 2):
        ptr1, ptr2 = s[i], s[len(s) - 1 - i]
        if ptr1 != ptr2:
            return False
    return True


def is_palindrome_2(s: str) -> bool:
    """check if the given string is a palindrome

    >>> isPalindrome("A man, a plan, a canal: Panama")
    True
    """
    s = s.replace(" ", "")
    s = s.lower()
    s = "".join(char for char in s if char.isalpha())
    return s == s[::-1]
