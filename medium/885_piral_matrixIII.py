"""
885. Spiral Matrix III

You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.
"""
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        steps = 1
        x, y = rStart, cStart
        d = 0

        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    if 0 <= x < rows and 0 <= y < cols:
                        result.append([x, y])
                    x += directions[d][0]
                    y += directions[d][1]
                d = (d + 1) % 4
            steps += 1

        return result