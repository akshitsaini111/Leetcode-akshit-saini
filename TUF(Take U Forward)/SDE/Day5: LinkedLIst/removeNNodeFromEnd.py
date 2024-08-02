class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNEnd(self, head, k):
        dummy = node(0, head)
        left = dummy
        right = head

        for _ in range(k):
            right = right.next

        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
