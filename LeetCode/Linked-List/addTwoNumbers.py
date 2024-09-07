class ListNode:

    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1, l2):
        dmmy = ListNode(0)
        curr = dmmy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + carry
            carry = v // 10
            v = v % 10
            curr.next = ListNode(v)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dmmy.next


# tmux
