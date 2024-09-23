from collections import deque


class Solution:

    def KnightMove(self, targetPosition, startPosition, N):
        visited = set()
        q = deque()
        directions = [
            (2, 1),
            (2, -1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (1, -2),
            (-1, -2),
        ]

        sp = (startPosition[0] - 1, startPosition[1] - 1)
        tp = (targetPosition[0] - 1, targetPosition[1] - 1)

        q.append([sp[0], sp[1], 0])
        visited.add((sp[0], sp[1]))

        while q:
            for _ in range(len(q)):
                x, y, l = q.popleft()

                if x == tp[0] and y == tp[1]:
                    return l

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or ny < 0 or nx >= N or ny >= N or (nx, ny) in visited:
                        continue
                    q.append([nx, ny, l + 1])
                    visited.add((nx, ny))

        return -1
