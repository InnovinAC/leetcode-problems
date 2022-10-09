class Solution:
    def containsDuplicate(self, nums):
      if len(nums) == len(set(nums)):
        return False
      return True
      
      
      '''
      #####################
              OR
      ##################### 
      '''
          
from collections import Counter
class Solution:
    def containsDuplicate(self, nums):
      nums = dict(Counter(nums))
      a = [v for k, v in nums.items() if v > 1]
      if len(a) > 0:
        return True
      return False
