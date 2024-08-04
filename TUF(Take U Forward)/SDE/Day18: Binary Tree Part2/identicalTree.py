class node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def same(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.same(p.lef, q.left) and self.same(p.right, q.right)
        return False
