class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def reOrder(self, head):
        # Finding The Middle Point
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second Half
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # joing the both the list
        first = head
        second = prev
        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
