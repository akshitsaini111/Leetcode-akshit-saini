class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inOrderTraversal(self, root):
        res = []

        def inOrder(node):
            if node:
                inOrder(node.left)
                res.append(node.val)
                inOrder(node.right)

        inOrder(root)
        return res
