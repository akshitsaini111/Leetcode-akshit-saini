class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def treeBuilder(self, nums):
        if not nums:
            return
        mid = len(nums) // 2
        root = Node(nums[mid])
        root.left = self.treeBuilder(nums[:mid])
        root.right = self.treeBuilder(nums[mid + 1 :])
        return root


nums = [-10, -3, 0, 5, 9]
sol = Solution()
ans = sol.treeBuilder(nums)
print("The Tree From Sorted Array Is:", ans)
