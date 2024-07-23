class Solution:

    def subSets(self, arr):
        n = len(arr)
        res = []

        def dfs(i, sub):
            if i >= len(arr):
                res.append(sub[::])
                return
            sub.append(arr[i])
            dfs(i + 1, sub)
            sub.pop()
            dfs(i + 1, sub)

        dfs(0, [])
        return res


arr = [1, 2, 3]
sol = Solution()
print("Answer is", sol.subSets(arr))


# arr=[1,2,3]
