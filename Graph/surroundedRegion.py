class Solution:
    def surrounded(self,grid):
        R=len(grid)
        C=len(grid)
        visit=set()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or (r,c) in visit or grid[r][c]!="O":
                return 
            grid[r][c]="T"
            visit.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)

        for r in range(R):
            for c in range(C):
            
