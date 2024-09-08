class Solution:

    def reverse(self, s):
        i = 0
        j = 0
        n = len(s)

        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        while j < n:
            if s[j] == " ":
                reverse(s, i, j - 1)
                i = j + 1
            elif j == n - 1:
                reverse(s, i, j)

        reverse(s, 0, n - 1)
