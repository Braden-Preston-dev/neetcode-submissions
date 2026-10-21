class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        chosen = [False] * len(nums)
        def backtrack(combo):
            if len(combo) == len(nums):
                res.append(combo[:])
                return
            
            for i in range(len(nums)):
                if not chosen[i]:
                    combo.append(nums[i])
                    chosen[i] = True
                    backtrack(combo)
                    combo.pop()
                    chosen[i] = False

        backtrack([])
        return res