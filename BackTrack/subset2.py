class Solution:

    def subSet(self, arr):
        arr.sort()
        res = []

        def dfs(i, sub):
            if i >= len(arr):
                res.append(sub[::])
                return
            sub.append(arr[i])
            dfs(i + 1, sub)
            sub.pop()
            while i + 1 < len(arr) and arr[i + 1] == arr[i]:
                i += 1
            dfs(i + 1, sub)

        dfs(0, [])
        return res


arr = [1, 2, 3, 3, 2, 4]
sol = Solution()
print(sol.subSet(arr))
