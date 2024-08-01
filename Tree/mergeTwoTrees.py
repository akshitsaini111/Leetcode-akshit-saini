class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def merge(self, root1, root2):
        if not root1 and not root2:
            return
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        v = v1 + v2
        root = Node(v)
        root.left = self.merge(
            root1.left if root1 else None, root2.left if root2 else None
        )
        root.right = self.merge(
            root1.right if root1 else None, root2.right if root2 else None
        )
        return root
