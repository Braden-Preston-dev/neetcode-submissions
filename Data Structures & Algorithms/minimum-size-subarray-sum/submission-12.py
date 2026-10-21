class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l, r = 0, 0
        sums = 0
        shortest = 100001

        while r < len(nums):
            sums += nums[r]
            while sums >= target and l <= r:
                shortest = min(shortest, r - l + 1)
                sums -= nums[l]
                l += 1
            r += 1 
        return shortest if shortest < 100001 else 0