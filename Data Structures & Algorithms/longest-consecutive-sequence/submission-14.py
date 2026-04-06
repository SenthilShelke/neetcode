class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in nums:
                sequenceLength = 0
                while nums[i] + sequenceLength in nums:
                    sequenceLength += 1
                longest = max(longest, sequenceLength)

        return longest