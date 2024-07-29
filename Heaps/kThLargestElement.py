import heapq


class Solution:

    def KthLarget(self, nums, k):
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums)
        return abs(res)
