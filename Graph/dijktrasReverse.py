import heapq


class Solution:

    def dReverse(self, n, edges, start_node, end_node):
        adj = {i: [] for i in range(n)}
        for s, d, w in edges:
            adj[s].append([d, w])

        longest = {}
        maxHeap = [[-1.0, start_node]]

        while maxHeap:
            w1, n1 = heapq.heappop(maxHeap)
            currWeight = -w1

            if n1 == end_node:
                return currWeight

            if n1 in longest:
                continue

            longest[n1] = currWeight

            for n2, w2 in adj[n1]:
                if n2 in longest:
                    continue
                temp = currWeight * w2
                heapq.heappush(maxHeap, [-temp, n2])
        return 0
