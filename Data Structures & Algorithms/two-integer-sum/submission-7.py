class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        sol = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in sol:
                return [sol[complement], i]
            sol[nums[i]] = i
        return 0
