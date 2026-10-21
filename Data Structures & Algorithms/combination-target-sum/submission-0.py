class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(i, sums, sub):
            if sums == target:
                res.append(sub[ : ])
                return
            elif sums > target or i >= len(nums): return

            sub.append(nums[i])

            backtrack(i, sums + nums[i], sub)

            sub.pop()

            backtrack(i + 1, sums, sub)

        backtrack(0, 0, [])

        return res
            
