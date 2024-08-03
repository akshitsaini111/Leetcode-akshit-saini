class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def rotate(self, head, k):
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return head
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        tail.next = head
        return new_head
