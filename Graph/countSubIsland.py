class Solution:

    def subIsland(self, grid1, grid2):
        R = len(grid1)
        C = len(grid1[0])
        count = 0
        visit = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= R
                or c >= C
                or grid2[r][c] == 0
                or (r, c) in visit
            ):
                return True
            res = True
            visit.add((r, c))
            if grid1[r][c] == 0:
                res = False
            for dr, dc in directions:
                res = dfs(r + dr, c + dc) and res
            return res

        for r in range(R):
            for c in range(C):
                if grid2[r][c] and (r, c) not in visit and dfs(r, c):
                    count += 1
        return count
