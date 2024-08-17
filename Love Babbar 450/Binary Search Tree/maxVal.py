class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxVal(self, root):
        if not root:
            return
        curr = root
        while curr.right:
            curr = curr.right
        return curr.val
