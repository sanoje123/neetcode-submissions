class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        max_area = 0

        def bfs(r, c):
            area = 0
            q = collections.deque()
            q.append((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            while q:
                r, c = q.popleft()
                grid[r][c] = 0
                area += 1
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==1:
                        q.append((row, col))
                        grid[row][col] = 0
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    max_area = max(area, max_area)
        
        return max_area
