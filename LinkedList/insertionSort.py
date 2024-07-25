class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If the list is empty or has only one node, it is already sorted
        if not head or not head.next:
            return head

        # Create a dummy node which acts as the new head of the sorted part of the list
        dummy = ListNode(0)
        curr = head

        # Traverse the original list
        while curr:
            # At each iteration, we insert curr into the correct position in the sorted part of the list
            prev = dummy

            # Find the correct position to insert curr
            while prev.next and curr.val >= prev.next.val:
                prev = prev.next

            # Insert curr into the sorted part
            next_node = curr.next  # Store the next node to process after insertion
            curr.next = prev.next  # Insert curr after prev
            prev.next = curr  # Update prev.next to point to curr
            curr = next_node  # Move to the next node in the original list

        return dummy.next  # The sorted list starts after the dummy node


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
