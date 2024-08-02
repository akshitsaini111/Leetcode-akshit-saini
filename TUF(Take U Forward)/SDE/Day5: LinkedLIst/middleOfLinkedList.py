class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def middle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
