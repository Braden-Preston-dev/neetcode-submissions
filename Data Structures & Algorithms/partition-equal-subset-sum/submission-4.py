class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        half = sum(nums) // 2
        if sum(nums) % 2 != 0: return False
        cache = [[-1] * (half + 1) for _ in range(n)]

        def dfs(i, cur):
            if cur == half: return True
            if i >= len(nums) - 1 or cur >= half: return False
            if cache[i][cur] != -1: return cache[i][cur]

            cache[i][cur] = dfs(i + 1, cur) or dfs(i + 1, cur + nums[i])
            return cache[i][cur]

        return dfs(0, 0)