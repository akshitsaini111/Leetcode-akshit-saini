class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def leafSimilar(self, root1, root2):
        def dfs(node, res):
            if not node:
                return
            if not node.left and node.right:
                res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)

        r1 = dfs(root1, [])
        r2 = dfs(root2, [])

        return r1 == r2
