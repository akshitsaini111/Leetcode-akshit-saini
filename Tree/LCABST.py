class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SOlution:

    def LCA(self, root, p, q):
        curr = root
        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.right
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.left
            else:
                return curr
        return None
