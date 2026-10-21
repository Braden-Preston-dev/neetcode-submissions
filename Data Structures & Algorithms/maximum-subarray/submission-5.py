class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curSum = 0
        maxSum = nums[0]
        i = 0
        while i < len(nums):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)
            i += 1
        
        return maxSum

