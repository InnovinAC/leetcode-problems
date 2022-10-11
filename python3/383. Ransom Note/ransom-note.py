class Solution:
    def canConstruct(self, ransomNote, magazine):
        boolsss = []
        for x in magazine:
            if x in ransomNote:
                magazine = magazine.replace(x, "")
                boolsss.append("t")
            else:
                boolsss.append("f")
                break
        if "f" in boolsss:
            return False
        else:
            return True
                
