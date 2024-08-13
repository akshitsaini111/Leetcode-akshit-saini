from collections import deque


class Solution:

    def shortestDistanceInMatrix(self, grid):
        R = len(grid)
        C = len(grid[0])
        visit = set()
        q = deque()
        q.append([0, 0, 1])
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
            [1, 1],
            [-1, -1],
            [1, -1],
            [-1, 1],
        ]
        while q:
            for _ in range(len(q)):
                r, c, l = q.popleft()
                if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 1:
                    continue
                if r == R - 1 and c == C - 1:
                    return l
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr >= R or nc >= C or (nr, nc) in visit:
                        continue
                    q.append((nr, nc, l + 1))
                    visit.add((nr, nc))
        return -1
