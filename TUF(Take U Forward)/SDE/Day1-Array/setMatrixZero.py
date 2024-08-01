class Solution:

    def setMatrixZero(self, grid):
        R = len(grid)
        C = len(grid[0])
        row = set()
        col = set()

        # first iteration to locate all the zero
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    row.add(r)
                    col.add(c)

        # second iteration to make that row and col to 0
        for r in range(R):
            for c in range(C):
                if r in row or c in col:
                    grid[r][c] = 0
        return grid
