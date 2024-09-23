from collections import deque


class Solution:

    def bfs(self, adj):
        n = len(adj)
        q = deque()
        res = []
        visit = set()
        q.append(0)
        visit.add(0)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node)

                for nei in adj[node]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)

        return res
