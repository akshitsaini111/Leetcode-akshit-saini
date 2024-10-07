class Solution:

    def coutPrime(self, n):
        if n <= 2:
            return 0
        ref = [True] * n

        i = 2
        while (i * i) < n:
            if ref[i]:
                for j in range(i * i, n, i):
                    ref[j] = False
            i += 1

        ans = ref.count(True) - 2
        return ans
