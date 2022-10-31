class Solution:
    
    def heightChecker(self, heights):
        a = sorted(heights)
        count = 0
        for x, y in enumerate(heights):
          if heights[x] != a[x]:
            count += 1
        return count
