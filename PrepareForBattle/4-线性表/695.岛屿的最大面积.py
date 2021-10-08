# -*- coding: utf-8 -*-
from collections import deque


def maxAreaOfIsland(grid) -> int:
    n = len(grid)
    p = len(grid[0])
    queue = deque([])
    direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    max_area = 0

    for i in range(n):
        for j in range(p):
            if (grid[i][j] == 0) or (grid[i][j] == 2):
                continue
            else:
                area = 1
                queue.append([i, j])
                grid[i][j] = 2

                while queue:
                    (x0, y0) = queue.popleft()
                    for (x, y) in direct:
                        if (0 <= x0 + x < n) and (0 <= y0 + y < p):
                            if grid[x0 + x][y0 + y] == 1:
                                area += 1
                                queue.append((x0 + x, y0 + y))
                                grid[x0 + x][y0 + y] = 2

                max_area = max(max_area, area)
                
    return max_area
