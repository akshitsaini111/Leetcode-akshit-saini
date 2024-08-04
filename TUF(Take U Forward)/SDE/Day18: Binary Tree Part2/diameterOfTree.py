class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameter(self, root):
        res = [0]

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            d = l + r
            res[0] = max(res[0], d)
            return 1 + max(l, r)

        dfs(root)
        return res[0]
