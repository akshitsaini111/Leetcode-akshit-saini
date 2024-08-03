from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def topView(self, root):
        tv = {}
        q = deque()
        q.append((root, 0))
        while q:
            node, hd = q.popleft()
            if hd not in tv:
                tv[hd] = node.val
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        sk = sorted(tv.keys())
        res = [tv[hd] for hd in sk]
        return res
