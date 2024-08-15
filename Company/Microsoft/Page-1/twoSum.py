class Solution:

    def twoSum(self, nums, target):
        difference = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in difference:
                return [difference[diff], i]
            difference[n] = i
        return -1
