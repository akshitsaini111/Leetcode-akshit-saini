class node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def balancedBinaryTree(self, root):
        def dfs(node):
            if not node:
                return [0, True]
            l = dfs(node.left)
            r = dfs(node.right)
            balanced = l[1] and r[1] and abs(l[0] - r[0]) <= 1
            return [1 + max(l[0], r[0]), balanced]

        res = dfs(root)
        return res[1]
