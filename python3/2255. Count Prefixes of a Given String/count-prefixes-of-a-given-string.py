// Solution 1
class Solution:
    def countPrefixes(self, words, s):
      my_list = []
      i = 1
      while i < len(s) + 1:
        my_list.append(s[0:i])
        i+=1
      
      count = 0
      for x in words:
        if x in my_list:
          count += 1
      return count
      
      
      
// Solution 2
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
      return sum(map(s.startswith, words))
