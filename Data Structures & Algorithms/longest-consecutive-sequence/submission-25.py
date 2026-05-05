class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        nums.sort()
        longest = 0

        for i in range(len(nums)):
            longestSequence = 0
            while nums[i] + longestSequence in numSet:
                longestSequence += 1
            longest = max(longest, longestSequence)

        return longest


# 0, 1, 1, 2, 3, 4, 5, 6