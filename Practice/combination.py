class Solution:

    def combination(self, n, k):
        res = []

        def backTrack(i, sub):
            if len(sub) == k:
                res.append(sub[::])
                return
            for j in range(i, n + 1):
                sub.append(j)
                backTrack(j + 1, sub)
                sub.pop()

        backTrack(1, [])
        return res
