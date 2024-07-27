class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solotion:

    def Pallindrome(self, head):
        # first Find the middle of the linked List
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the linked list
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        second = prev
        while second:
            if second.val != first.val:
                return False
            first = first.next
            second = second.next

        return True
