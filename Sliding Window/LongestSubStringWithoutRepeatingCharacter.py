class Solution:

    def longestSubstringWithoutRepeatingCharacter(self, s):
        l = 0
        visit = set()
        res = 0
        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])
            res = max(res, r - l + 1)
        return res
