class Solution:
    def searchInsert(self, nums, target):
      if target not in nums:
        nums.append(target)
        nums = sorted(nums)
      return nums.index(target)
        
