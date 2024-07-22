class Solution:
    def parameterOfIsland(self,grid):
        R=len(grid)
        C=len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or  grid[r][c]==0:
                return 1
            if grid[r][c]==-1:
                return 0
            grid[r][c]=-1
            peri=0
            for dr, dc in directions:
                peri+=dfs(r+dr,c+dc)
            return peri
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    return dfs(r,c)

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

sol=Solution()
print(sol.parameterOfIsland(grid))
