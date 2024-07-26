class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        curr = head
        while curr:
            prev = dummy

            while prev.next and curr.val >= prev.next.val:
                prev = prev.next

            curr.next, prev.next, curr = prev.next, curr, curr.next
        return dummy.next


# Example usage:
# Let's create a linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

# Create a Solution object
sol = Solution()

# Sort the linked list using insertion sort
sorted_head = sol.insertionSortList(head)


# Function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Print the sorted linked list
print_list(sorted_head)  # Output: 1 -> 2 -> 3 -> 4 -> None
