class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid: return 0

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):

            q = deque()
            grid[row][col] == "0"
            q.append((row, col))

            while q:
                level = len(q)

                for i in range(level):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc

                        if r not in range(rows) or c not in range(cols) or grid[r][c] == "0":
                            continue
                        q.append((r, c))
                        grid[r][c] = "0"

            

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1

        return count