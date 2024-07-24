class Solution:

    def combinationSum(self, nums, target):
        res = []

        def dfs(i, sub, total):
            if total == target:
                res.append(sub[::])
                return
            if i >= len(nums) or total > target:
                return

            sub.append(nums[i])
            dfs(i, sub, total + nums[i])
            sub.pop()
            dfs(i + 1, sub, total)

        dfs(0, [], 0)
        return res


sol = Solution()
nums = [2, 3, 6, 7]
target = 7
print("Combination Sum", sol.combinationSum(nums, target))
