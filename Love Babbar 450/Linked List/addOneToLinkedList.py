class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def addOne(self, head):
        num = 0
        curr = head
        while curr:
            num = num * 10 + curr.val
            curr = curr.next

        num += 1

        dummy = Node(0)
        curr = dummy
        while num > 0:
            new_digt = num % 10
            num = num // 10
            curr.next = Node(new_digt)
            curr = curr.next

        reversed_list = dummy.next
        curr = reversed_list
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
