class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = "".join(x for x in s if x.isalnum())
      original = s.lower()
      s = s.lower()[::-1]
      if original == s:
        return True
      return False
        
