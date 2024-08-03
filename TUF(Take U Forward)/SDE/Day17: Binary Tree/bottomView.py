from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bottomView(self, root):
        q = deque()
        q.append((root, 0))
        bv = {}
        while q:
            node, hd = q.popleft()
            bv[hd] = node.val
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        sorted_keys = sorted(bv.keys())
        res = [bv[hd] for hd in sorted_keys]
        return res
