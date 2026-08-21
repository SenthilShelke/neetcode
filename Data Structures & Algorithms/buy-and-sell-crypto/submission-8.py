class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        left = 0
        right = 1
        while right != len(prices):
            profit = prices[right] - prices[left]
            maximum = max(maximum, profit)
            if prices[right] < prices[left]:
                left = right
                right = left + 1
            elif prices[right] >= prices[left]:
                right += 1

        return maximum

# max = 1