class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        while i < len(s):
            if not s[i].isalnum():
                s = s.replace(s[i], "")
            i += 1

        original = s.lower()

        s = "".join(reversed(s))
        
        s = s.lower()

        if original == s:
            return True
        else:
            return False