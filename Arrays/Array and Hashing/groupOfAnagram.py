class Solution:

    def groupOfAnagram(self, strs):
        res = {}
        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word in res:
                res[sorted_word].append(i)
            else:
                res[sorted_word] = [i]
        return list(res.values())
