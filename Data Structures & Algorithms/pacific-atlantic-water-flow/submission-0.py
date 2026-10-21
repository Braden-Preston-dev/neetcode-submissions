class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return [[]]
        
        atlantic, pacific = set(), set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = []
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, prev):
            if (r, c) in visited or r < 0 or r == rows or c < 0 or c == cols or prev > heights[r][c]: return
            visited.add((r, c))
            prev = heights[r][c]
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                dfs(row, col, visited, prev)

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
            dfs(0, c, pacific, heights[0][c])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append([r, c])
        return res

        


        