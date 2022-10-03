class Solution:
    def romanToInt(self, s):
        new_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        new_sum = 0
        for x, y in enumerate(s):
            if x+1 < len(s):
                if new_dict[y] < new_dict[s[x+1]]:
                    new_sum -= new_dict[y]
                else:
                    new_sum += new_dict[y]
            else:
                new_sum += new_dict[y]
        return new_sum
    
        
