class Solution:

    def noOfProvinces(self, grid):
        n = len(grid)
        visited = set()
        count = 0

        def dfs(i):
            visited.add(i)

            for j in range(n):
                if grid[i][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count
