class Solution:
    def climbStairs(self, n):
      a, b = 1, 1+n%2
      for i in range(int(n/2)):
        a += b
        b += a
      return a
