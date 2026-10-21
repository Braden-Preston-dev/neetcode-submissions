class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def backtrack(i, combo, sums):
            if sums == target:
                res.append(combo[:])
                return
            elif sums > target or i >= len(candidates): return

            combo.append(candidates[i])

            backtrack(i + 1, combo, candidates[i] + sums)

            combo.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
                
            backtrack(i + 1, combo, sums)
        
        backtrack(0, [], 0)

        return res