class Solution:
    def rotateString(self, s, goal):
      length = len(s)
      i = 0
      
      while i < length:
        s = s[1:] + s[0]
        if s == goal:
          return True
        i += 1
      return False
