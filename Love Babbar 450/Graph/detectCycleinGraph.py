class Solution:

    def detectCycle(self, adj):
        n = len(adj)
        visiting = set()
        visited = set()

        def dfs(i):
            if i in visiting:
                return False
            if i in visited:
                return True

            visiting.add(i)
            for nei in adj[i]:
                if dfs(nei) == False:
                    return False
            visiting.remove(i)
            visited.add(i)
            return True

        for i in range(n):
            if dfs(i) == False:
                return False
        return True
