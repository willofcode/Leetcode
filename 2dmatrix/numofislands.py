class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge case of empty matrix
        if not grid:
            return 0
        # defining the dimension
        rows, cols = len(grid), len(grid[0])
        # up, down, right, left
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # track visited, avoiding cycle and revisit
        visited = set()
        # intialized count for islands
        islands = 0

        def dfs(r, c):
            # out of bound condition
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return
            # track visited to avoid recursion
            visited.add((r,c))
            # marks the cell as visited directly in the grid,
            # a mutation step that helps prevent re-traversal of the same land cell.
            grid[r][c] = "0"
            # traverse in all 4 adjacent directions
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1

        return islands
        
        # time complexity: O(m*n)
        # space complexity: O(m*n)
            
            
