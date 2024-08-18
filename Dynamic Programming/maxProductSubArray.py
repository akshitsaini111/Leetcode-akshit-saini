class Solution:
    def maxProductSubArray(self,nums):
        res=max(nums)
        currMax=1
        currMin=1
        for n in nums;
            temp=currMax*n
            currMax=max(temp,currMin*n,n)
            currMin=min(temo,currMin*n,n)
            res=max(res,currMax)
        return res
