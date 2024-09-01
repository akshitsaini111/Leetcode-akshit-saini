from collections import deque


class Solution(object):

    def shorestDistanceToTreasure(self, grid):
        R = len(grid)
        C = len(grid[0])
        visit = set()
        q = deque()
        dist = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        nr < 0
                        or nc < 0
                        or nr >= R
                        or nc >= C
                        or grid[nr][nc] == -1
                        or (nr, nc) in visit
                    ):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
            dist += 1
