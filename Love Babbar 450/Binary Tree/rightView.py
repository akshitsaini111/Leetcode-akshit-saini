from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def leftView(self, root):
        q = deque()
        q.append(root)
        res = []
        while q:
            right = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    right = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if right:
                res.append(right.val)
        return res
