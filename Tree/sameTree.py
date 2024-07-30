class node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def same(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.same(p.left, q.left) and self.same(p.right, q.right)
        return False
