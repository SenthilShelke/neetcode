class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dp(total):
            if total == amount:
                return 0
            elif total > amount:
                return float('inf')
            else:
                if total in cache:
                    return cache[total]
                minCost = float('inf')
                for coin in coins:
                    minCost = min(minCost, 1 + dp(total + coin))
                cache[total] = minCost
                return minCost

        if dp(0) == float('inf'):
            return -1
        else:
            return dp(0)
                