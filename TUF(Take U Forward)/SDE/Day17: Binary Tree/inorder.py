class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorder(self, root):
        res = []

        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)

        dfs(root)
        return res
