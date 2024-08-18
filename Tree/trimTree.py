class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def trimTree(self, root, low, high):
        if not root:
            return
        if root.val < low:
            return self.trimTree(root.right, low, high)
        if root.val > high:
            return self.trimTree(root.left, low, high)
        root.left = self.trimTree(root.left, low, high)
        root.right = self.trimTree(root.right, low, high)
        return root
