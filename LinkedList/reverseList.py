class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse(self, head):
        if not head:
            return
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


def printLL(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next


def createLinkedList(vals):
    if not vals:
        return
    head = ListNode(vals[0])
    curr = head
    for i in range(1, len(vals)):
        curr.next = ListNode(vals[i])
        curr = curr.next
    return head


vals = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
head = createLinkedList(vals)
print("Original List")
sol = Solution()
printLL(head)
reversedList = sol.reverse(head)
print("-----------------------------------------------------------------------")
print("Reversed List")
printLL(reversedList)
