class Solution:
    def addBinary(self, a, b):
      a, b = int(a, 2), int(b, 2)
      c = str(bin(a + b))
      return c[2:]
