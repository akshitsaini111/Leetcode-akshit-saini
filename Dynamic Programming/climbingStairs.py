# Bottom UP -Approach
class Solution:

    def noOfWays(self, n):
        one = 1
        two = 1
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
