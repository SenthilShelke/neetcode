class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dp(i, sum):
            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0
            else:
                if (i, sum) in cache:
                    return cache[(i, sum)]
                add = dp(i + 1, sum + nums[i])
                sub = dp(i + 1, sum - nums[i])
                count = add + sub
                cache[(i, sum)] = count
                return count

        return dp(0, 0)