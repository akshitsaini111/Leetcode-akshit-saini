class Solution:

    def validPallindrome(self, s):
        res = ""
        for i in s:
            if i.isalnum():
                res += i.lower()
        return res == res[::-1]
