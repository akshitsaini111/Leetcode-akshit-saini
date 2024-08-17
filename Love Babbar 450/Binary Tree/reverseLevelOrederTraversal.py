from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def reverseLevelOrderTraversal(self, root):
        q = deque()
        q.append(root)
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level:
                res.append(level)

        n = len(res)
        ans = []
        for i in range(n - 1, -1, -1):
            for j in res[i]:
                ans.append(j)
        return ans
