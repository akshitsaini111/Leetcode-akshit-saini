# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def verticalTraversal(self, root):
        m2 = dict()
        k = [0]

        def helper(root, level, depth):
            if not root:
                return
            k[0] = min(k[0], level)
            if level not in m2:
                m2[level] = []
            m2[level].append((depth, root.val))
            helper(root.left, level - 1, depth + 1)
            helper(root.right, level + 1, depth + 1)

        helper(root, 0, 0)
        res = []
        while k[0] in m2:
            curr = sorted(m2[k[0]])
            des = []
            for i in curr:
                des.append(i[1])
            res.append(des)
            k[0] += 1
        return res
