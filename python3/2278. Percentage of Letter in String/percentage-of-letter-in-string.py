class Solution:
    def percentageLetter(self, s, letter):
        return int(s.count(letter)/len(s) * 100)
