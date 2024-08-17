class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minVal(self, root):
        if not root:
            return
        curr = root
        while curr.left:
            curr = curr.left
        return curr.val
