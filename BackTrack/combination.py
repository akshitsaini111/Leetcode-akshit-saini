class Solution:

    def combination(self, n, k):
        res = []

        def dfs(i, sub):
            if len(sub) == k:
                res.append(sub[::])
                return

            for j in range(i, n + 1):
                sub.append(j)
                dfs(j + 1, sub)
                sub.pop()

        dfs(1, [])
        return res


n = 4
k = 2
sol = Solution()
print("combination", sol.combination(n, k))
