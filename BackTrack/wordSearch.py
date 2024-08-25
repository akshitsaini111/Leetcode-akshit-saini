class Solution:

    def wordSearch(self, grid, word):
        R = len(grid)
        C = len(grid[0])
        visit = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= R or c < 0 or c >= C or word[i] != grid[r][c]:
                return False
            visit.add((r, c))
            res = (
                dfs(r + 1, c, i + 1),
                dfs(r - 1, c, i + 1),
                dfs(r, c + 1, i + 1),
                dfs(r, c - 1, i + 1),
            )
            visit.remove((r, c))
            return res

        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False
