class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def partition(self, head, x):
        left = node(0)
        right = node(0)
        lt = left
        rt = right
        curr = head
        while curr:
            if curr.val < x:
                lt.next = curr
                lt = lt.next
            else:
                rt.next = curr
                rt = rt.next
            curr = curr.next
        lt.next = right.next
        rt.next = None
        return left.next
