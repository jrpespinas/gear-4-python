from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly-linked list

    >>> linked_list = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1, None)))))
    >>> head = reverse_list(linked_list)
    >>> print_list(head)
    1
    2
    3
    4
    5
    """
    curr = head
    nextN, prev = None, None
    while curr != None:
        nextN = curr.next
        curr.next = prev
        prev = curr
        curr = nextN
    return prev


def print_list(head: Optional[ListNode]):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.next
