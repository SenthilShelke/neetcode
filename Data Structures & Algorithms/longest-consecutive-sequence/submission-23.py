class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maximum = 0

        for i in range(len(nums)):
            longestSequence = 0
            while nums[i] + longestSequence in numSet:
                longestSequence = longestSequence + 1
            maximum = max(maximum, longestSequence)
            

        return maximum