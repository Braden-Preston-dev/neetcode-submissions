class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        minNum = 1
        inc = set()
        for num in nums:
            
            if num > 0 and minNum >= num:
                minNum = num + 1
                while minNum in inc:
                    minNum += 1
            inc.add(num)
        return minNum
