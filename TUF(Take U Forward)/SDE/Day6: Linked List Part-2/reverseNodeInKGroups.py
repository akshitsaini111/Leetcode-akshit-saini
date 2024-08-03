class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverseKGroup(self, head, k):
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        gp = dummy  # Group previous (the node before the group to be reversed)

        while True:
            # Find the k-th node
            kth = self.getKth(gp, k)
            if not kth:
                break

            # Reverse k nodes'
            next_group = kth.next
            prev, curr = kth.next, gp.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect reversed group back to the previous part
            gp.next, gp = kth, gp.next
        return dummy.next

    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
