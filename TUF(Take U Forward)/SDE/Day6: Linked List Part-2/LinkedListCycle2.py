class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def detectCycle(self, head):
        visit = set()
        curr = head
        while curr:
            if curr in visit:
                return curr
            else:
                visit.add(curr)
                curr = curr.next
        return None
