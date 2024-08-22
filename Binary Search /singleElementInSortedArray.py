class Solution:

    def singleElementInSortedArray(self, nums):
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for i in count:
            if count[i] == 1:
                return True
        return False
