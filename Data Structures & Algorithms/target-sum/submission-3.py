class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dp(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            else:
                if (i, total) in cache:
                    return cache[(i, total)]
                add = dp(i + 1, total + nums[i])
                sub = dp(i + 1, total - nums[i])
                ans = add + sub
                cache[(i, total)] = ans
                return ans

        return dp(0, 0)
