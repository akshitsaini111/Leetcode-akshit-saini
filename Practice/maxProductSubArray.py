class Solution:

    def maxProductSubArray(self, n):
        res = max(n)
        cMax = 1
        cMin = 1
        for i in n:
            temp = cMax * i
            cMax = max(temp, i * cMin, i)
            cMin = min(temp.i * cMin, i)
            res = max(res, cMax)
        return res
