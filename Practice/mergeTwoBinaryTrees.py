class Node:

    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def mergeTwoTrees(self, tree1, tree2):
        if not tree1 and not tree2:
            return

        v1 = tree1.val if tree1 else 0
        v2 = tree2.val if tree2 else 0
        v = v1 + v2
        root = Node(v)
        root.right = self.mergeTwoTrees(
            tree1.right if tree1 else None, tree2.right if tree2 else None
        )

        root.left = self.mergeTwoTrees(
            tree1.left if tree1 else None, tree2.left if tree2 else None
        )

        return root
