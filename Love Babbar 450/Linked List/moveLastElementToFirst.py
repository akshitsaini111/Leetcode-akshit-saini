class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SOlution:

    def moveLastElementToFirst(self, head):
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        curr = head
        for _ in range(length - 2):
            curr = curr.next

        curr.next = None
        tail.next = head
        return tail
