class node:

    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:

    def copyRandomPointer(self, head):
        copy = {None: None}
        curr = head
        while curr:
            temp = curr.val
            copy[curr] = node(temp)
            curr = curr.next

        curr = head
        while curr:
            node = copy[curr]
            node.next = copy[curr.next]
            node.random = copy[curr.random]
            curr = curr.next
        return copy[head]
