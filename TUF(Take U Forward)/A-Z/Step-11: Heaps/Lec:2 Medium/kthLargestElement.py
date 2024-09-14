import heapq


class Solution:

    def kthLargestElement(self, nums, k):
        nums = [-i for i in nums]
        heapq.heapify(nums)
        ans = -1
        for _ in range(k):
            ans = heapq.heappop(nums)

        return -ans
