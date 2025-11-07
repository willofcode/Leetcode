class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # base case, 
        # if board[][] == surrounded, mark S
        # stopping condition
        # we want to implement DFS because we want to verify DFS
        if not board:
            return

        row, col = len(board), len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != 'O':
                return 
            
            board[r][c] = 'S'
            
            for dr,dc in dirs:
                dfs(r + dr, c + dc)

        for r in range(row):
            for c in range(col):
                if r == 0 or c == 0 or r == (row-1) or c == (col-1):
                    if board[r][c] == 'O':
                        dfs(r,c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "S":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
  
        # time complexity: O(M * N) for rows and columns in the matrix
        # space complexity: O(M * N) recursive stack
        
