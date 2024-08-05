class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeSort(self, head):
        if not head or head.next:
            return head

        left = head
        mid = self.getMid(head)
        right = mid.next
        mid.next = None

        l_sort = self.mergeSort(left)
        r_sort = self.mergeSort(right)

        return self.merge(l_sort, r_sort)

    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l1, l2):
        dummy = node(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        return dummy.next
