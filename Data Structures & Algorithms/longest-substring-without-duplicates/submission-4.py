class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        left = 0
        charSet = set()
        charSet.add(s[left])
        
        for right in range(1, len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            longest = max(longest, len(charSet))

        return longest

