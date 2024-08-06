class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def insertionSort(self, head):
        if not head or not head.next:
            return
        dummy = Node(0)
        curr = head
        while curr:
            prev = dummy
            while prev.next and curr.val >= prev.next.val:
                prev = prev.next
        curr.next, prev.next, curr = prev.next, curr, curr.next
        return dummy.next
