class Solution:

    def containsDuplicate(self, nums):
        n = set(nums)
        return True if len(nums) != len(n) else False
