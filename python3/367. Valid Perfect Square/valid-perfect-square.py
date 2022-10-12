class Solution:
    def isPerfectSquare(self, num):
      a,b = 0, 1
      while a < num:
        a += b
        b += 2
      return a==num
