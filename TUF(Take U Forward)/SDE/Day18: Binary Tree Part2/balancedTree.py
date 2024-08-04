class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def balanced(self, root):
        def dfs(node):
            if not node:
                return [0, True]
            l = dfs(node.left)
            r = dfs(node.right)
            bal = l[1] and r[1] and abs(l[0] - r[0]) <= 1
            return [1 + max(l[1], r[0]), bal]

        res = dfs(root)
        return res[1]
