import heapq


class Solution:

    def dijktrasToTarget(self, n, edges, src, target):
        adj = {i: [] for i in range(n)}
        for s, d, w in edges:
            adj[s].append([d, w])

        short = {}
        minHeap = [[0, src]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in short:
                continue
            short[n1] = w1

            if n1 == target:
                print(w1)
                break
            for n2, w2 in adj[n1]:
                if n2 in short:
                    continue
                heapq.heappush(minHeap, [w1 + w2, n2])

        return -1
