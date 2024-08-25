class Node:

    def __init__(self, val, neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors


class Solution:

    def cloneGraph(self, root):
        copy = {}

        def dfs(node):
            if node in copy:
                return copy[node]
            temp = Node(node.val)
            copy[node] = temp
            for nei in node.neighbors:
                temp.neighbors.append(dfs(nei))
            return temp

        return dfs(root) if root else None
