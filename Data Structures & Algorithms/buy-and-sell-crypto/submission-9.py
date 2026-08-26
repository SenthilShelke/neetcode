class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maximum = 0
        while right != len(prices):
            profit = prices[right] - prices[left]
            maximum = max(profit, maximum)
            if prices[right] <= prices[left]:
                left = right
                right = left + 1
            else:
                right += 1

        return maximum
            