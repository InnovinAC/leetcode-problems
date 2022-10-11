class Solution:
    def lengthOfLastWord(self, s):
      new_list = s.split()
      return len(new_list[-1])
