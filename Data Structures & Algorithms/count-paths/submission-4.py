class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ROWS, COLS = m - 1, n - 1
        cache = [[-1] * n for _ in range(m)]
        count = 0

        def dfs(i, j):
            nonlocal count
            if i == ROWS and j == COLS: return 1
            if i > ROWS or j > COLS: return 0
            if cache[i][j] != -1: return cache[i][j]

            cache[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return cache[i][j]
        
        return dfs(0, 0)