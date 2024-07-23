class Solution:

    def noOfIsland(self, grid):
        R = len(grid)
        C = len(grid[0])
        count = 0
        directions = [[2, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                return

            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    dfs(r, c)
                    count += 1
        return count
