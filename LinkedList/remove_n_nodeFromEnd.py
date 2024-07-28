class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNodeFromEnd(self, head, n):
        dummy = node(0, head)
        curr = head
        prev = dummy

        for _ in range(n):
            curr = curr.next

        while curr:
            prev = prev.next
            curr = curr.next
        prev.next = prev.next.next

        return dummy.next
