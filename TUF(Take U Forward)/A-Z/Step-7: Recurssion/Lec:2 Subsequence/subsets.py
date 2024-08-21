class SOlution:

    def subsets(self, nums):
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
        return res
