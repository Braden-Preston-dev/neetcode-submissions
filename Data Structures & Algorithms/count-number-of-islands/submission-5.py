class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        islands = 0

        def dfs(r, c):
            if (r, c) in visited: return

            visited.add((r, c))

            for dr, dc in directions:
                row, col = dr + r, c + dc
                if row in range(rows) and col in range(cols) and grid[row][col] == "1":
                    dfs(row, col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands
