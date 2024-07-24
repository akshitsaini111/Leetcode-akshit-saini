class Solution:

    def permutation(self, nums):
        res = []
        if len(nums) == 1:
            return [nums[::]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permutation(nums)
            for perm in perms:
                perm.append(n)
                res.append(perm)
            nums.append(n)
        return res


n = [1, 2, 3]
sol = Solution()
print("Permutaion", sol.permutation(n))
