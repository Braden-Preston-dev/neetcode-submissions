class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = [-1] * len(cost)

        def dfs(i, cache):
            if i >= len(cost): return 0
            if cache[i] != -1: return cache[i]
            cache[i] = cost[i] + min(dfs(i + 1, cache), dfs(i + 2, cache))
            return cache[i]

        return min(dfs(0, cache), dfs(1, cache))
            
