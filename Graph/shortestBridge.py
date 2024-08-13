from collections import deque


class Solution:

    def shortesBridge(self, grid):
        R = len(grid)
        C = len(grid[0])
        visit = set()
        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                return
            q.append((r, c))
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            count = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if nr < 0 or nc < 0 or nr >= R or nc >= C or (nr, nc) in visit:
                            continue
                        if grid[nr][nc] == 1:
                            return count
                        q.append((nr, nc))
                        visit.add((nr, nc))
                count += 1
            return count

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()
