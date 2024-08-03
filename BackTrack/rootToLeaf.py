class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def paths(self, root):
        def dfs(node, path, paths):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                dfs(node.left, path, paths)
                dfs(node.right, path, paths)
            path.pop()

        paths = []
        dfs(root, [], paths)
        return paths
