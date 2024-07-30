from collections import deque


class node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def zigZag(self, root):
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
                level = reversed(level) if len(res) % 2 else level
                res.append(level)
        return res
