class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = nums1[0:m]
        nums1.clear()
        nums1 += a
          
        nums1 += nums2
        nums1.sort()
