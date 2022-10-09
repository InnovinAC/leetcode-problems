class Solution:
    def isValid(self, s):
        bracket_dict = {}
        bracket_dict["("] = ")"
        bracket_dict["["] = "]"
        bracket_dict["{"] = "}"

        list = [i for i in s]
        
        for i in list:
            item = bracket_dict[i]
            if item in s:
                list.remove(item)
                continue
            else:
                return False
        return True
