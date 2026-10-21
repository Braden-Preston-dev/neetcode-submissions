class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}

        def dfs(amount):
            if amount == 0: return 0
            if amount in cache: return cache[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0: 
                    res = min(1 + dfs(amount - coin), res)
            cache[amount] = res
            return res
        
        res = dfs(amount) 

        return res if res != 1e9 else -1