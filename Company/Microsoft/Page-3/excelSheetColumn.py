class Solution(object):

    def excelSheetColumn(self, string):
        count = 0
        for c in string:
            characterValue = ord(c) - ord("a") + 1
            count = count * 26 + characterValue
        return count
