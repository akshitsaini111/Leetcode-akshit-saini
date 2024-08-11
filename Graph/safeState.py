class Solution:

    def safeState(self, graph):
        safe = {}
        res = []

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if dfs(i) == False:
                    return False
            safe[i] = True
            return True

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
