class Solution:

    def validAnagram(self, s, t):
        if len(s) != len(t):
            return False
        charS = {}
        charT = {}
        for i in s:
            charS[i] = 1 + charS.get(i, 0)
        for j in t:
            charT[j] = 1 + charT.get(j, 0)
        return charS == charT
