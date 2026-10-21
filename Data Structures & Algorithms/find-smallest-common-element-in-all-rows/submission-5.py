class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        seen = []
        rows, cols = len(mat), len(mat[0])
        
        
        for r in range(1, rows):
            inRow = set()
            for c in range(cols):
                inRow.add(mat[r][c])
            seen.append(inRow)

        for c in range(cols):
            find = mat[0][c]
            count = 0
            for s in seen:
                if find not in s:
                    break
                count += 1
            if count == len(mat) - 1: return find
        
        return -1
