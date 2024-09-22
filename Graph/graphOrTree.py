class Solution:

    def graphOrTree(self, edges, n):
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visted = set()

        def dfs(node, prev):
            if node in visted:
                return False
            visted.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node) == False:
                    return False
            return True

        return dfs(0, -1) and len(visted) == n
