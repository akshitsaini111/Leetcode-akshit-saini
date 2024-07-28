class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def rotateLinkedList(self, head, k):
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        right = head
        for _ in range(length - k - 1):
            right = right.next

        new_head = right.next
        right.next = None
        tail.next = head
        return new_head
