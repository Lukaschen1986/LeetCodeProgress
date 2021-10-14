# -*- coding: utf-8 -*-
from collections import defaultdict


def leastBricks(wall) -> int:
    """
    穿过的砖块数量最少 = n - 穿过的缝隙数量最多
    """
    dct = defaultdict(int)
    n = len(wall)

    for i in range(n):
        lst = wall[i]
        for j in range(len(lst)):
            key = sum(lst[:j])  # 神来之笔
            dct[key] += 1

    dct.pop(0)
    if dct:
        max_val = max(dct.values())
        return n - max_val
    else:
        return n


if __name__ == "__main__":
    wall = [
        [1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1]
    ]
    wall = [[1], [1], [1]]
    res = leastBricks(wall)
    print(res)
