import heapq


class Solution:

    def kthSmallestElement(self, nums, k):
        heapq.heapify(nums)
        ans = float("inf")
        for _ in range(k):
            ans = heapq.heappop(nums)

        return ans
