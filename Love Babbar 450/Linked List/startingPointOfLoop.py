class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def startingPointOfLoop(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None