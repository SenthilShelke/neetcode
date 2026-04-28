class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dp(i):
            if i == len(cost):
                return 0
            elif i > len(cost):
                return float('inf')
            else:
                if i in cache:
                    return cache[i]
                oneStep = cost[i] + dp(i + 1)
                twoSteps = cost[i] + dp(i + 2)
                ans = min(oneStep, twoSteps)
                cache[i] = ans
                return ans

        return min(dp(0), dp(1))
