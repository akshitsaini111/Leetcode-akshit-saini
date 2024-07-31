class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def subTree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        if self.same(root, subRoot):
            return True
        return self.subTree(root.left, subRoot) and self.subTree(root.right, subRoot)

    def same(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.same(p.left, q.left) and self.same(p.right, q.right)
        return False
