# Boiler Plate to create node class and to print and create a linked list


class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def createLinkedList(vals):
    if not vals:
        return
    head = node(vals[0])
    curr = head
    for i in range(1, len(vals)):
        curr.next = node(vals[i])
        curr = curr.next
    return head


def printLL(head):
    if not head:
        return
    while head:
        print(head.val, end="->" if head.next else "\n")
        head = head.next


vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
head = createLinkedList(vals)
printLL(head)
