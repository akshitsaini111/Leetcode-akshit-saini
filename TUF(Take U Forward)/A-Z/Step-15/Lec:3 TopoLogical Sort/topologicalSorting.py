class Solution:

    def topologicalSort(self, V, adj):
        visiting = set()
        visited = set()
        res = []

        def dfs(j):
            if j in visiting:
                return False
            if j in visited:
                return True
            visiting.add(j)
            for nei in adj[j]:
                if dfs(nei) == False:
                    return False
            visiting.remove(j)
            visited.add(j)
            res.append(j)
            return True

        for i in range(V):
            if dfs(i) == False:
                return []
        return res[::-1]
