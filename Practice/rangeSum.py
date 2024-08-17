class Node:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rangeSum(self, root, low, high):
        res = [0]

        def dfs(node):
            if not node:
                return
            if low <= node.val <= high:
                res[0] += node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res[0]
