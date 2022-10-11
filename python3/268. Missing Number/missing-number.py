class Solution:
    def missingNumber(self, nums):
      nums_count = len(nums) + 1
      nums = set(nums)
      
      new_set = set(range(0, nums_count))
      
      return list(new_set.difference(nums))[0]
      
      
        
