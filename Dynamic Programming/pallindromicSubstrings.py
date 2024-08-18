class Solution:

    def pallSub(self, s):
        def exp(s, l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count

        res = 0
        for i in range(len(s)):
            res += exp(s, i, i)
            res += exp(s, i, i + 1)
        return res
