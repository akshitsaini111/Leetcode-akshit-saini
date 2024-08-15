# trbl->S
class Solution:

    def spiralMatrix(self, grid):
        # top
        t = 0
        # Left
        l = 0
        # Right
        r = len(grid[0])
        # bottom
        b = len(grid)
        res = []

        while l < r and t < b:
            # Traversing left to right
            for i in range(l, r):
                res.append(grid[l][i])
            t += 1

            # Traversing from top-right to right-bottom

            for i in range(t, b):
                res.append(grid[i][r - 1])
            r -= 1

            # we do no want to traverse extra
            if not (l < r and t < b):
                break

            # traversing from right-bottom to left-bottom
            for i in range(r - 1, l - 1, -1):
                res.append(grid[b - 1][i])
            b -= 1

            # traversing from bottom-left toward up
            for i in range(b - 1, t - 1, -1):
                res.append(grid[i][l])
            l += 1
        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol = Solution()
print("Spiral Matrix", sol.spiralMatrix(matrix))
