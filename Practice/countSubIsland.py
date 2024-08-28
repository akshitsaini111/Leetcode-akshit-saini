class Solution:

    def subIsland(self, grid1, grid2):
        R = len(grid2)
        C = len(grid2[0])
        visit = set()
        count = 0

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= R
                or c >= C
                or (r, c) in visit
                or grid2[r][c] == 0
            ):
                return True
            res = True
            visit.add((r, c))
            if grid1[r][c] == 0:
                res = False
            res = dfs(r + 1, c) and res
            res = dfs(r, c + 1) and res
            res = dfs(r - 1, c) and res
            res = dfs(r, c - 1) and res
            return res

        for r in range(R):
            for c in range(C):
                if grid2[r][c] and (r, c) not in visit and dfs(r, c):
                    count += 1
        return count
