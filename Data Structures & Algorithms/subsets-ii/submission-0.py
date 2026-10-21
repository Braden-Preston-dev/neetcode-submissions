class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        def backtrack(combo, i):
            if i == len(nums):
                res.append(combo[:])
                return
            
            combo.append(nums[i])

            backtrack(combo, i + 1)

            combo.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(combo, i + 1)

        backtrack([], 0)
        return res
