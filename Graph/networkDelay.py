import heapq


class SOlution:

    def networkDelay(self, edges, n, k):
        adj = {i: [] for i in range(n + 1)}
        for s, d, t in edges:
            adj[s].append([d, t])

        short = {}
        minHeap = [[0, k]]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in short:
                continue
            short[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 in short:
                    continue
                heapq.heappush(minHeap, [w1 + w2, n2])

        res = max(short.values()) if len(short) == n else -1
        return res
