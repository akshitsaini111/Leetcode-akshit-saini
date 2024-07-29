from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def leftSide(self, root):
        res = []
        q = deque()
        q.append(root)
        while q:
            left = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    left = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if left:
                res.append(left.val)
        return res
