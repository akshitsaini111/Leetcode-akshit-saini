#Checking Astro vim

class Solution:
    def maxAreaOfIsland(self,grid):
        R=len(grid)
        C=len(grid[0])
        res=float("-inf")

        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or grid[r][c]==0:
                return 0
            grid[r][c]=0            
            area=1
            area+=dfs(r+1,c)
            area+=dfs(r-1,c)
            area+=dfs(r,c+1)
            area+=dfs(r,c-1)
            return area


        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    res=max(res,dfs(r,c))
        return res


grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

sol=Solution()
print(sol.maxAreaOfIsland(grid))
