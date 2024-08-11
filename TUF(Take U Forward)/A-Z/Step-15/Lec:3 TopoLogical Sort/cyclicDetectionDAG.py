class Solution:

    def cycleDetection(self, v, adj):
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
            visited.add(j)
            visiting.remove(j)
            return False

        for i in range(v):
            if dfs(i):
                return True
        return False
