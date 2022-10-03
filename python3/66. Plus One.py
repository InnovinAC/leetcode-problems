class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      digits = list(map(str, digits))
      integer = int("".join(digits))
      integer += 1
      
      return list(str(integer))
        
