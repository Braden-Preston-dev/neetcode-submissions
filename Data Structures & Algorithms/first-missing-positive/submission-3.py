class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        minNum = 1
        n = set(nums)

        while minNum in n:

            minNum += 1
        
        return minNum
