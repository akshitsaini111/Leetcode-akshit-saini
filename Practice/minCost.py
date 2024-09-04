class Solution:

    def minCost(self, n):
        n.append(0)
        for i in range(len(n) - 3, -1, -1):
            n[i] += min(n[i + 1], n[i + 2])
        return min(n[0], n[1])
