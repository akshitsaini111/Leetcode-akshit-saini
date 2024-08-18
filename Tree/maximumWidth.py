from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxWidth(self, root):
        q = deque()
        q.append([root, 1, 0])
        prevLevel = 0
        prevNum = 1
        res = 0
        while q:
            node, num, level = q.popleft()
            if level > prevLevel:
                prevLevel = level
                prevNum = num
            res = max(res, num - prevNum + 1)
            if node.left:
                q.append([node.left, num * 2, level + 1])
            if node.right:
                q.append([node.right, num * 2 + 1, level + 1])
        return res
