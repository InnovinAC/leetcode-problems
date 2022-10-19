class Solution:
    def findMaxK(self, nums):
      while 1:
        x = max(nums)
        if -x in nums:
          return x
        elif -x not in nums:
          nums.remove(x)
          if not nums:
            return -1
