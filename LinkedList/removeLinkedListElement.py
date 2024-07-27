class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def remove(self, head, target):
        while head and head.val == target:
            head = head.next
        prev = Node(0)
        curr = head
        while curr:
            if curr.val == target:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
