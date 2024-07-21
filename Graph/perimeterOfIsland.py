class Solution:
    def perimeter(self,grid):
        #Rows of Grid
        R=len(grid)
        #Columns of Grid
        C=len(grid[0])
        
        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or grid[r][c]==0:
                return 1
            # if we get a visited island
            if grid[r][c]==-1:
                return 0
            # Isalnd that we have visited
            grid[r][c]=-1
            perimeter=dfs(r+1,c)
            perimeter+=dfs(r,c+1)
            perimeter+=dfs(r-1,c)
            perimeter+=dfs(r,c-1)
            return perimeter
        
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

print(sol.perimeter(grid=grid))
        