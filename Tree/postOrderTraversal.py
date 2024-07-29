class node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def postOrder(self, root):
        res = []

        def dfs(node):
            if node:
                dfs(root.left)
                dfs(root.right)
                res.append(root.val)

        dfs(root)
        return res
