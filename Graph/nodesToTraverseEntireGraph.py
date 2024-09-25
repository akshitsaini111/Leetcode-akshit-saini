class Solution:

    def minimumNode(self, n, edges):
        adj = {i: [] for i in range(n)}
        res = []
        for src, dst in edges:
            adj[dst].append(src)

        for i in range(n):
            if adj[i] == []:
                res.append(i)

        return res
