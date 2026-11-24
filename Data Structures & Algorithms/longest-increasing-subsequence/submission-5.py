class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        cache = {}
        maxNum = max(nums)

        def dfs(i):
            if nums[i] == maxNum or i == len(nums) - 1: return 1
            if i in cache: return cache[i]
            
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    cache[i] = max(cache.get(i, 0), 1 + dfs(j))
            return 1 if i not in cache else cache[i]

        res = 0

        for n in range(len(nums)):
            res = max(dfs(n), res)

        return res