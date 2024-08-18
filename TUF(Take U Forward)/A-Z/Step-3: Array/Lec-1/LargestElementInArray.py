class Solution:

    def largest(self, nums):
        ans = nums[0]
        for i in nums:
            if i > ans:
                ans = i
        return ans


sol = Solution()
nums = [1, 4, 5, 7, 2, 3, 55, 67]
res = sol.largest(nums)
print("Largest Number", res)
