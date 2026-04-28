class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            longestSequence = 0
            while nums[i] + longestSequence in numSet:
                longestSequence += 1
            longest = max(longest, longestSequence)

        return longest