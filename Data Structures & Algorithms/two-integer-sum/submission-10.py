class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        res = []
        saved = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in saved:
                return [saved[complement], i]

            saved[nums[i]] = i
        return []