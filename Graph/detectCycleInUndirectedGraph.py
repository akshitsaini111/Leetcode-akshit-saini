class Soluiton:

    def detectCycle(self, n, edges):
        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()

        def dfs(i, prev):
            if i in visit:
                return True
            visit.add(i)

            for nei in adj[i]:
                if nei == prev:
                    continue
                if dfs(nei, i):
                    return True
            return False

        return dfs(0, -1)
