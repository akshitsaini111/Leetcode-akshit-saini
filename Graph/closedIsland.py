class Solution:

    def closedIsland(self, grid):
        R = len(grid)
        C = len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if grid[r][c] == 1 or (r, c) in visit:
                return True
            visit.add((r, c))
            top = dfs(r + 1, c)
            bottom = dfs(r - 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            return top and bottom and left and right

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0 and (r, c) not in visit:
                    if dfs(r, c):
                        res += 1
        return res


grid = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
]

sol = Solution()
print(sol.closedIsland(grid=grid))
