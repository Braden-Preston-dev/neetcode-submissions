class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = 0
        r = l = 0

        while r < len(nums) - 1:
            furthest = nums[l] + l
            for j in range(l, r + 1):
                furthest = max(furthest, nums[j] + j)

            l = r + 1
            r = furthest
            res += 1
        
        return res
