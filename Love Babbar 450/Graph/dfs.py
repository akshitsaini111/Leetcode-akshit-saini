class Solution:

    def dfs(self, adj):
        n = len(adj)
        visited = set()
        res = []

        def dfss(node, prev):
            if node in visited:
                return
            visited.add(node)
            res.append(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                dfss(nei, node)

            return

        dfss(0, -1)

        return res
