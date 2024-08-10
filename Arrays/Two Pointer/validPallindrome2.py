class Solution:

    def valPall2(self, s):
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                left_string = s[l + 1 : r + 1]
                right_string = s[l:r]
                return (
                    left_string == left_string[::-1]
                    or right_string == right_string[::-1]
                )
            l += 1
            r -= 1
        return True
