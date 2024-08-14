class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, num1, num2):
        first = self.createNumber(num1)
        second = self.createNumber(num2)

        total = first + second
        dummy = Node(0)
        curr = dummy
        # Now we will break this integer
        while total > 0:
            new_digit = total % 10
            total = total // 10
            curr.next = Node(new_digit)
            curr = curr.next

        reversed_list = dummy.next
        # now we will reverse The linked List
        curr = reversed_list
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def createNumber(self, head):
        nums = 0
        curr = head
        while curr:
            nums = nums * 10 + curr.val
            curr = curr.next
        return nums
