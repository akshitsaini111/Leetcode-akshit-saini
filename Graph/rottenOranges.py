from collections import deque


class Solution:

    def rottenOranges(self, grid):
        R = len(grid)
        C = len(grid[0])
        fresh = 0
        time = 0
        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        nr < 0
                        or nc < 0
                        or nr >= R
                        or nc >= C
                        or (nr, nc) in visit
                        or grid[nr][nc] != 1
                    ):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
