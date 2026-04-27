class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dp(i, total):
            if i >= len(nums):
                return 0
            else:
                if (i, total) in cache:
                    return cache[(i, total)]
                skip = dp(i + 1, total)
                rob = nums[i] + dp(i + 2, total)
                ans = max(skip, rob)
                cache[(i, total)] = ans
                return ans
             
        return dp(0, 0)