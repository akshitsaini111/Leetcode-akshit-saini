class node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def insert(self, root, val):
        if not root:
            return node(val)
        if val > root.val:
            root.right = self.insert(root.right, val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        return root
