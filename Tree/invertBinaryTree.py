class node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class solution:

    def invert(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.invert(root.left)
            self.invert(root.right)
        return root
