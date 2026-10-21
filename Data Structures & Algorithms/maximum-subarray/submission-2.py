class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # if len(nums) == 1: return nums[0]
        curSum = 0
        maxSum = -9999999
        i = 0
        while i < len(nums):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)
            i += 1
        
        return maxSum

