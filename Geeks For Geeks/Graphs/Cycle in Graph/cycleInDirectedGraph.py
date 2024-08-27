class Solution:

    def detectCycle(self, n, adj):
        visiting = set()
        visited = set()

        def dfs(j):
            if j in visiting:
                return True
            if j in visited:
                return False
            visiting.add(j)
            for nei in adj[j]:
                if dfs(nei):
                    return True
            visiting.remove(j)
            visited.add(j)
            return False

        for i in range(n):
            if dfs(i):
                return True
        return False
