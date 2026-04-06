class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        while i < len(s):
            if not s[i].isalnum():
                s = s.replace(s[i], "")
            i += 1

        s = s.lower()
        
        original = s

        s = "".join(reversed(s))

        if original == s:
            return True
        else:
            return False