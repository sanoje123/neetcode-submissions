class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        border_o_visited = set()

        border_o = collections.deque()
        # find al the border o: 
        for r in [0, ROWS - 1]:
            for c in range(COLS):
                if board[r][c] == "O":
                   border_o.append((r, c))
                   border_o_visited.add((r, c))

        for r in range(ROWS):
            for c in [0, COLS - 1]:
                if board[r][c] == "O":
                   border_o.append((r, c))
                   border_o_visited.add((r, c))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while border_o:
            r, c = border_o.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and (row, col) not in border_o_visited and board[row][col] == "O":
                    border_o.append((row, col))
                    border_o_visited.add((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in border_o_visited:
                    board[r][c] = "X" 
        
