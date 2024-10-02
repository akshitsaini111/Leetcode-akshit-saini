class Solution:

    def numberOfConnectedGraph(self, n, edges):
        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        count = 0

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for nei in adj[i]:
                dfs(nei)

            return

        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        return count
