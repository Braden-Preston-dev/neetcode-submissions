class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)

            if profit > 0: r += 1
            else: 
                l += 1
                r = l + 1

        return maxProfit