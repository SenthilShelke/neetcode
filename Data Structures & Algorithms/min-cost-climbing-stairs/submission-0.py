class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dp(i, costTaken):
            if i == len(cost):
                return 0
            elif i > len(cost):
                return float('inf')
            else:
                if (i, costTaken) in cache:
                    return cache[(i, costTaken)]
                oneStep = dp(i + 1, costTaken + cost[i])
                twoSteps = dp(i + 2, costTaken + cost[i])
                ans = cost[i] + min(oneStep, twoSteps)
                cache[(i, costTaken)] = ans
                return ans

        return min(dp(0, 0), dp(1, 0))