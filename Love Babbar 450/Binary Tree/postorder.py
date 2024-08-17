class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def postorder(self, root):
        res = []

        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                res.append(node.val)

        dfs(root)
        return res
