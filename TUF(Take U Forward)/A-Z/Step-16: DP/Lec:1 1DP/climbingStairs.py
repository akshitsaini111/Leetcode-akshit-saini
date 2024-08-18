# Fibonacci Series
class Solution:

    def numberOfWaysToClimb(self, n):
        one = 1
        two = 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
