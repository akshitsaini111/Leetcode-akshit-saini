class Solution:

    def intersection(self, nums1, nums2):
        res = list(set(nums1) & set(nums2))
        return res
