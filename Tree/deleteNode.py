class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deleteNode(self, root, key):
        if not root:
            return

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.lcie = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.left:
                return root.right
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        return root
