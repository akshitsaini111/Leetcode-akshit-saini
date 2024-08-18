class Solution:

    def maxSumOfNonAdjacent(self, nums):
        r1 = 0
        r2 = 0
        for n in nums:
            temp = max(r1 + n, r2)
            r1 = r2
            r2 = temp
        return r2
