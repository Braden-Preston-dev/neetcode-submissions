class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: return 0

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):

            grid[row][col] = "0"

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r >= 0 and c >= 0 and r < rows and c < cols and grid[r][c] == "1": dfs(r, c)
            

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and grid[i][j] not in visited:
                    dfs(i, j)
                    count += 1

        return count