class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()


        # def addCell(r, c):

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        steps = 0
        while q:
            steps += 1
            level = len(q)

            for i in range(level):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] < steps or (r, c) in visited:
                        continue
                    q.append((r, c))
                    visited.add((r, c))
                    grid[r][c] = steps





            