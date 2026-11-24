class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        cache = [-1] * len(nums)
        maxNum = max(nums)

        def dfs(i):
            if nums[i] == maxNum or i == len(nums) - 1: return 1
            if cache[i] != -1: return cache[i]
            
            LIS = 1
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    LIS = max(LIS, 1 + dfs(j))
            
            cache[i] = LIS
            return LIS

        return max(dfs(i) for i in range(len(nums)))