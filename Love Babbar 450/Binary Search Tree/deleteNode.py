class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deletNode(self, root, key):
        if not root:
            return
        if key > root.val:
            root.right = self.deletNode(root.right, key)
        elif key < root.val:
            root.left = self.deletNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deletNode(root.right, curr.val)
        return root
