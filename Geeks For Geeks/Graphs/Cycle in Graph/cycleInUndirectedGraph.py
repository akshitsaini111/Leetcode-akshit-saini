class Solution:

    def detectCycle(self, n, edges):
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()

        def dfs(i, parent):
            if i in visit:
                return True
            visit.add(i)
            for j in adj[i]:
                if j == parent:
                    continue
                if dfs(j, i):
                    return True
            return False

        return dfs(0, -1)
