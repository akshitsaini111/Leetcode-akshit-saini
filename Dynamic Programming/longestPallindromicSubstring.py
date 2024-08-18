class Solution:

    def longestPallindromicSubstring(self, s):
        def expandFromCeter(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        res = ""
        for i in range(len(s)):
            # odd Palindrome

            op = expandFromCeter(s, i, i)
            if len(op) > len(res):
                res = op

            # even Palindrome
            ev = expandFromCeter(s, i, i + 1)
            if len(ev) > len(res):
                res = ev

        return res
