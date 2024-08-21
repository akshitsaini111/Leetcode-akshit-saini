class Solution:

    def longest(self, s, k):
        l = 0
        count = {}
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = (r - l + 1, res)
        return res
