class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0

        for i in range(len(nums)):
            longestSequence = 0
            while nums[i] + longestSequence in nums:
                longestSequence += 1
            longest = max(longest, longestSequence)

        return longest
