class Solution:
        def removeElement(self, nums, val):
            original_nums = nums.copy()
            if len(nums) == 0:
                nums = [1]
        
            else:
                for y in original_nums:
                    if y == val:
                        nums.remove(y)
            
            return len(nums)
