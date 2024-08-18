class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def duplicateSubTree(self, root):
        sub = {}
        res = []

        def dfs(node):
            if not node:
                return "NULL"

            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if s in sub:
                if sub[s] == 1:
                    sub[s] += 1
                    res.append(s)
            else:
                sub[s] = 1
            return s

        dfs(root)
        return res
