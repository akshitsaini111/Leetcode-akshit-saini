class Solution:

    def safeState(self, graph):
        safe = {}
        res = []
        n = len(graph)

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False

            for nei in graph[i]:
                if dfs(nei) == False:
                    return False
            safe[i] = True

        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
