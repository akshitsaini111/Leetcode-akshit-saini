class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseLinkedlist(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
