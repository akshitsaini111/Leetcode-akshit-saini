class Solution:

    def houseRobber2(self, nums):
        return max(self.maxRob(nums[1:]), self.maxRob(nums[:-1]))

    def maxRob(self, n):
        rob1 = 0
        rob2 = 0
        for i in n:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
