class Solution:

    def setZero(self, grid):
        R = len(grid)
        C = len(grid[0])
        row = set()
        col = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    row.add(r)
                    col.add(c)

        for r in range(R):
            for c in range(C):
                if r in row or c in col:
                    grid[r][c] = 0

        return grid
