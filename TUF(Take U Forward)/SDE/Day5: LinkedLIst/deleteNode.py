class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next
