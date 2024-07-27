class Node:

    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class Solution:

    def merge(self, l1, l2):
        if not l1 and not l2:
            return

        dummy = Node(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next


def createLinkedList(vals):
    if not vals:
        return

    head = Node(vals[0])
    curr = head
    for i in range(1, len(vals)):
        curr.next = Node(vals[i])
        curr = curr.next

    return head


def printLinkedList(head):
    while head:
        print(head.val, end="->" if head.next else "\n")
        head = head.next


vals1 = [1, 3, 5, 7, 9]
l1 = createLinkedList(vals1)
print("First Linked List")
printLinkedList(l1)
print("------------------------------------------")
vals2 = [2, 4, 6, 8]
l2 = createLinkedList(vals2)
print("Second Linkde List")
printLinkedList(l2)
print("------------------------------------------")
sol = Solution()
mergedList = sol.merge(l1, l2)
print("Combined Linked List")
printLinkedList(mergedList)
