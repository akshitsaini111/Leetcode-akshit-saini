import heapq


class Solution:

    def dijktras(self, n, edges, start_node, end_node):
        adj = {i: [] for i in range(n)}
        for s, d, w in edges:
            adj[s].append([d, w])
            adj[d].append([s, w])

        short = {}
        minHeap = [[0, start_node]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 == end_node:
                return w1
            if n1 in short:
                continue
            short[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 in short:
                    continue
                heapq.heappush(minHeap, [w1 + w2, n2])
        return 0
