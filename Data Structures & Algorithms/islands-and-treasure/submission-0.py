class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])

        q = collections.deque()
        visited = set()

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # First add all the tresures in the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))

        while q:
            r, c, d = q.popleft()
            grid[r][c] = d
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(rows) and col in range(cols) and (row, col) not in visited and grid[row][col] != -1:
                    q.append((row, col, d + 1))
                    visited.add((row, col))
        