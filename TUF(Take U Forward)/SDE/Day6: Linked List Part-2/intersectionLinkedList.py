class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Soluiton:

    def intersection(self, headA, headB):
        l1 = headA
        l2 = headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
