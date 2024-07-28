class node:

    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:

    def mergeBetween(self, a, b, list1, list2):
        tail = list2
        while tail.next:
            tail = tail.next

        left = list1
        right = list1
        for _ in range(a - 1):
            left = left.next

        for _ in range(b + 1):
            right = right.next

        left.next = list2
        tail.next = right

        return list1
