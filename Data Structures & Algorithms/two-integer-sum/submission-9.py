class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        res = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in res:
                return [res[need], i]
            
            res[nums[i]] = i
            
        return []