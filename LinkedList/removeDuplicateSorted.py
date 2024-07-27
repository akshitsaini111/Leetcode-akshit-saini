class node:

    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
                continue
            else:
                curr = curr.next
        return head
