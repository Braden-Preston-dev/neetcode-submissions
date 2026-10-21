class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        maxArea = 0
        seen = set()


        def bfs(r, c):
            q = deque()
            q.append((r, c))
            seen.add((r, c))
            count = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if 0 > r or r >= rows or 0 > c or c >= cols or grid[r][c] == 0 or (r, c) in seen:
                        continue
                    seen.add((r, c))
                    q.append((r, c))
                    count += 1
            return count



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = bfs(r, c)
                    maxArea = max(area, maxArea)


        return maxArea
