# -*- coding: utf-8 -*-
from collections import deque


def closedIsland(grid) -> int:
    """
    只要陆地不触及到边界，就是封闭的
    """
    n = len(grid)
    p = len(grid[0])
    res = 0
    direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([])

    for i in range(n):
        for j in range(p):
            if (grid[i][j] == 1) or (grid[i][j] == 2):
                continue
            else:
                flag = True
                grid[i][j] = 2
                queue.append([i, j])

                while queue:
                    x0, y0 = queue.popleft()
                    for (x, y) in direct:
                        if (0 <= x0 + x < n) and (0 <= y0 + y < p):
                            if grid[x0 + x][y0 + y] == 0:
                                grid[x0 + x][y0 + y] = 2
                                queue.append([x0 + x, y0 + y])
                        else:
                            flag = False

                if flag:
                    res += 1

    return res


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ]
    res = closedIsland(grid)
    print(res)
