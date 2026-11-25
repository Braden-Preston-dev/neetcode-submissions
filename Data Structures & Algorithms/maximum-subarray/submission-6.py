class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        curMax = 0
        res = nums[0]

        for num in nums:
            tmp = curMax + num
            curMax = max(num, tmp)
            res = max(curMax, res)
        
        return res
