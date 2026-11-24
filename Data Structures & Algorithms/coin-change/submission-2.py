class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}

        def dfs(money):
            if money == amount: return 0
            if money in cache: return cache[money]

            minimum = 99999
            for c in coins:
                if money + c <= amount:
                    minimum = min(1 + dfs(money + c), minimum)
            cache[money] = minimum
            return minimum

        mincoins = dfs(0)
        print(mincoins)
        return -1 if mincoins >= 99999 else mincoins
