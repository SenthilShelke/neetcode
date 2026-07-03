class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dp(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in cache:
                return cache[(i, holding)]
            elif holding == True:
                sell = prices[i]
                keep = dp(i + 1, True)
                ans = max(sell, keep)
            else:
                buy = -prices[i] + dp(i + 1, True)
                skip = dp(i + 1, False)
                ans = max(buy, skip)
            cache[(i, holding)] = ans
            return ans

        return dp(0, False)