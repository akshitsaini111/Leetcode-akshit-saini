class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return
        if not l2:
            return l1
        if not l1:
            return l2

        dummy = node(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + carry
            carry = v // 10
            v = v % 10
            curr.next = node(v)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
