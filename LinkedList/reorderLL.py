class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def reOrder(self, head):
        # Finding The Middle Point
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second Half
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # joing the both the list
        first = head
        second = prev
        while second.next:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        return head


# Helper functions to print and create the linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


def create_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


# Example usage
values = [1, 2, 3, 4, 5]
head = create_list(values)
print("Original list:")
print_list(head)

solution = Solution()
reordered_head = solution.reOrder(head)
print("Reordered list:")
print_list(reordered_head)
