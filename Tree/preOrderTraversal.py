class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preOrder(self, root):
        res = []

        def dfs(node):
            if node:
                res.append(node.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return res
