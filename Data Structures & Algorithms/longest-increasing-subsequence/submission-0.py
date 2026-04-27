class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dp(i):
            if i == len(nums):
                return 0
            else:
                if i in cache:
                    return cache[i]
                longest = 1
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        longest = max(longest, 1 + dp(j))
                cache[i] = longest
                return longest

        arr = []
        for i in range(len(nums)):
            arr.append(dp(i))

        return max(arr)
