class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        count = {}

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1

            while (right - left + 1 - max(count.values())) > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            
        return longest

# k = 1
# A -> 4
# B -> 2



# r = 5
# l = 0