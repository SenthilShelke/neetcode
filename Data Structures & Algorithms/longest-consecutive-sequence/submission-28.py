class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            longest = 0
            while nums[i] + longest in nums:
                longest += 1
            res = max(res, longest)

        return res



# 2,3,4,4,5,10,20