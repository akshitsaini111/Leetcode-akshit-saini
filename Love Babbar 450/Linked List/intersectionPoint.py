class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def intersectionPoint(self, head1, head2):
        l1 = head1
        l2 = head2
        while l1 != l2:
            l1 = l1.next if l1 else head2
            l2 = l2.next if l2 else head1
        return l1
