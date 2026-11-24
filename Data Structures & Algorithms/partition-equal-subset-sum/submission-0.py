class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        half = sum(nums) / 2
        if sum(nums) % 2 != 0: return False
        cache = [[-1] * n for _ in range(n)]

        def dfs(i, cur):
            if cur == half: return True
            if i >= len(nums) - 1 or cur >= half: return False

            for j in range(i + 1, len(nums)):
                if cur + nums[j] <= half:
                    print(cur)
                    if dfs(j, cur + nums[j]): return True

            return False

        return any(dfs(i, 0) for i in range(len(nums)))