class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        N = len(prices)
        maxProfit = 0

        while r < N:
            
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)

            if prices[l] > prices[r]:
                l += 1
            else: r += 1
        return maxProfit