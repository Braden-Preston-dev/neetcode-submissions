class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i, k = 0, 0

        while i < len(nums):
            nums[k] = nums[i]
            k += 1
            if i + 2 < len(nums) and nums[i] == nums[i + 2]:
                i += 2
                while i < len(nums) - 1 and nums[i] == nums[i + 1]: 
                    i += 1
            else: i += 1

        return k
