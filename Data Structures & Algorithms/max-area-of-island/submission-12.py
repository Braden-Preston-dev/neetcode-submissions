class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        maxArea = 0

        def bfs(r, c):
            
            area = 1
            q = deque()
            q.append((r, c))
            grid[r][c] = 0

            while q:
                level = len(q)

                for i in range(level):
                    r, c = q.popleft()

                    for dr, dc in directions:
                        row = r + dr
                        col = c + dc
                        if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0: continue
                        q.append((row, col))
                        grid[row][col] = 0
                        area += 1
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(bfs(r, c), maxArea)

        return maxArea
