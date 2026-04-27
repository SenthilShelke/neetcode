class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dp(i, total):
            if i >= len(nums):
                return 0
            else:
                if (i, total) in cache:
                    return cache[(i, total)]
                robCurrent = dp(i + 1, total)
                robNext = nums[i] + dp(i + 2, total)
                ans = max(robCurrent, robNext)
                cache[(i, total)] = ans
                return ans
             
        return dp(0, 0)