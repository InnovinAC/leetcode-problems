from collections import Counter
class Solution:
    def firstUniqChar(self, s):
      my_dict = dict(Counter(s))
      my_list = [k for k,v in my_dict.items() if v == 1]
      if not my_list:
        return -1
      else:
        return s.find(my_list[0])
