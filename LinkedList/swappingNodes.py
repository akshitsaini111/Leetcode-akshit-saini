class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapNodes(self, head, n):
        left = head
        for _ in range(n - 1):
            left = left.next

        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1

        right = head
        for _ in range(length - n):
            right = right.next

        left.val, right.val = right.val, left.val

        return head
