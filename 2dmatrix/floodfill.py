class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # consider horizontal and vertically connected from source pixel
        # handle edge case
        if not image or not image[0]:
            return image
        # source pixel
        source = image[sr][sc]
        # Handle case where new color = old color
        if source == color:
            return image
        # defining the dimension, and adjacent direction
        rows, cols = len(image), len(image[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            # handles out of bound or if current pixel is not source pixel
            # fills region of the same pixel as source pixel (connected region)
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != source:
                return
            # update pixel upon visiting, handles "visited" tracking, no extra visited set needed.
            image[r][c] = color
            # recurse in all 4 adjacent direction
            for nr, nc in dirs:
                dfs(r + nr, c + nc)
        # start recursion from source
        dfs(sr,sc)
        return image

        # time complexity: O(m*n) for nth numnber of pixels in m x n dimension
        # space complexity: O(m*n) for call stack of dfs()


        # alternate implementation

        # rows, cols = len(image), len(image[0])
        # source = image[sr][sc]
        # if source == color:
        #     return image
        # def dfs(r, c):
        #     if image[r][c] == source:
        #         image[r][c] = color
        #         if r >= 1:
        #             dfs(r-1, c)
        #         if r + 1 < rows:
        #             dfs(r + 1, c)
        #         if c >= 1:
        #             dfs(r, c - 1)
        #         if c + 1 < cols:
        #             dfs(r, c + 1)

        # dfs(sr, sc)
        # return image
        
        # time complexity: O(m*n) for nth numnber of pixels
        # space complexity: O(m*n) for call stack of dfs
        
        
#        # implement BFS
#        src = image[sr][sc]
#        # handles infinite recursion, if source pixel is already color
#        if src == color:    # stop condition
#            return image
#        
#        row, col = len(image),len(image[0])
#        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
#        #
#        que = collections.deque([(sr,sc)])
#        # mark the starting pixel as recolored, ensured no cycle or revisiting
#        image[sr][sc] = color
#
#        while que:
#            # pop the front element (popleft()) ensuring FIFO order *BFS patter*
#            r, c = que.popleft()
#            for dr, dc in dirs:
#                # traverse in adjacent direction
#                nr, nc = r + dr, c + dc
#                # ensuring neighbor (nr, nc) still in designated region and inside the image boundaries
#                if 0 <= nr < row and 0 <= nc < col and image[nr][nc] == src:
#                    # recolored and marked as visited
#                    image[nr][nc] = color
#                    que.append((nr,nc)) # explore neighbor and append FIFO
#        
#        return image
