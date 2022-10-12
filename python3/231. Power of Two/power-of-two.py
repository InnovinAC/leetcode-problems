class Solution:
    def isPowerOfTwo(self, n):
      squares = [2**x for x in range(0,32)]
      return n in squares
