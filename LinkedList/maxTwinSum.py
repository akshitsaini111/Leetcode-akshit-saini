class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def maxTwin(self, head):
        # middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second Part
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        res = 0
        first = head
        second = prev
        while second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next
        return res
