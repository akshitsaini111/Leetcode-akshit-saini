class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def intersection(self, head1, head2):
        dummy = Node(0)
        curr = dummy
        l1 = head1
        l2 = head2

        while l1 and l2:
            if l1.val == l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
                l2 = l2.next
            elif l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
        return dummy.next
