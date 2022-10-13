from collections import Counter
class Solution:
    def isAnagram(self, s, t):
      t_dict = dict(Counter(t))
      s_dict = dict(Counter(s))
      if t_dict == s_dict:
        return True
      return False
