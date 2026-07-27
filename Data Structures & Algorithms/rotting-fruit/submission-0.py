class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque() # all the roten fruit at the begiining
        f_count = 0
        minut = 0
        visited = set()

        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    f_count += 1

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        v_fruit = 0
        while q:
            row, col, m = q.popleft()
            minut = max(m, minut)
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c]==1:
                    q.append((r, c, m + 1))
                    visited.add((r, c))
                    v_fruit += 1
        
        return minut if v_fruit == f_count else -1

        