class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}

        def dfs(i, cur):
            if i == len(nums):
                return cur == target
            if (i, cur) in cache: return cache[(i, cur)]


            cache[(i, cur)] = dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])
            return cache[(i, cur)]
        
        return dfs(0, 0)