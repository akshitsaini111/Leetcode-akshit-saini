class Solution:

    def validTree(self, n, edges):
        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()

        def dfs(i, parent):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if dfs(j, i) == False:
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
