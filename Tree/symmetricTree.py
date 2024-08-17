class Node:

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def symmetricTree(self, root):
        def dfs(right, left):
            if not right and not left:
                return True
            if not right or not left:
                return False
            return (
                right.val == left.val
                and dfs(right.right, left.left)
                and dfs(right.left, left.right)
            )

        return dfs(root.right, root.left)
