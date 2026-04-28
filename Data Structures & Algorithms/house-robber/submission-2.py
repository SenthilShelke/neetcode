class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dp(i):
            if i >= len(nums):
                return 0
            else:
                if i in cache:
                    return cache[i]
                rob = nums[i] + dp(i + 2)
                skip = dp(i + 1)
                ans = max(rob, skip)
                cache[i] = ans
                return ans

        return dp(0)