class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currMin = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < currMin: currMin = prices[i]
            elif prices[i] > currMin:
                profit += prices[i] - currMin
                currMin = prices[i]
        return profit