class Solution:

    def lenLastWord(self, sentence):
        words = sentence.split()
        return len(words[-1])
