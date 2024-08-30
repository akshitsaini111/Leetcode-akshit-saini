import heapq


class Solution:

    def shortestFromEachNode(self, n, edges, start):
        adj = {i: [] for i in range(n)}
        for src, dist, weight in edges:
            adj[src].append([weight, dist])
        shortest = {}
        minheap = [[0, start]]
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for w2, n2 in adj[n1]:
                if n2 in shortest:
                    continue
                heapq.heappush(minheap, [w1 + w2, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest
