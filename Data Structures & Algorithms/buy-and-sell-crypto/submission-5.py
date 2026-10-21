class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        N = len(prices)
        maxProfit = 0

        while r < N:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else: l = r
            r += 1
        return maxProfit