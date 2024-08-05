class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:

    def reverseKGroup(self, head, k):
        dummy = Node(0, head)
        gp = dummy

        while True:
            kth = self.getKth(gp, k)
            if not kth:
                break
            gn = kth.next
            prev = kth.next
            curr = gp.next
            while curr != gn:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            gp.next, gp = kth, gp.next

        return dummy.next

    def getKth(self, head, k):
        while head and k > 0:
            head = head.next
            k -= 1
        return head
