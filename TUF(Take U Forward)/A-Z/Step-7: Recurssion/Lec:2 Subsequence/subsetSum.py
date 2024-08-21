class Solution:

    def subsetSum(self, nums):
        res = []

        def dfs(i, sub):
            if i >= len(nums):
                res.append(sub[::])
                return
            sub.append(nums[i])
            dfs(i + 1, sub)
            sub.pop()
            dfs(i + 1, sub)

        dfs(0, [])
        ans = [sum(i) for i in res]
        return ans
