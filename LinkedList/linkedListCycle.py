class node:

    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:

    def cycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return True
        return False


def cycle(head):
    visited = set()
    curr = head
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False
