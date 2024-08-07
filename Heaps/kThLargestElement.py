import heapq


class Solution:

    def KthLarget(self, nums, k):
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums)
        return abs(res)


nums = [3, 2, 1, 5, 6, 4]
k = 2
sol = Solution()
ans = sol.KthLarget(nums, k)
print("Answer is :", ans)
