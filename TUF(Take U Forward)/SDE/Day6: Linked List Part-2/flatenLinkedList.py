class node:

    def __init__(self, val, next=None, bottom=None):
        self.val = val
        self.next = next
        self.bottom = bottom


class Solution:

    def flatten(self, head):
        if not head or not head.next:
            return head

        merged_head = self.flatten(head.next)
        head = self.merge(head, merged_head)
        return head

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = node(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.bottom = l1
                l1 = l1.bottom
            else:
                curr.bottom = l2
                l2 = l2.bottom
            curr = curr.bottom

        if l1:
            curr.bottom = l1
        if l2:
            curr.bottom = l2
        return dummy.bottom
