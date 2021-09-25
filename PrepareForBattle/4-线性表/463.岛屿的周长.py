# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:55:34 2021

@author: ASUS
其中恰好有一个岛屿
"""

def islandPerimeter(grid) -> int:
    n = len(grid)
    p = len(grid[0])
    res = 0
    
    def helper(i, j):
        direct = [(-1,0), (0,1), (1,0), (0,-1)]
        tmp = 0
        
        for (x,y) in direct:
            if (0 <= i+x < n) and (0 <= j+y < p):
                if grid[i+x][j+y] == 0:
                    tmp += 1
            else:
                tmp += 1
        
        return tmp
    
    
    for i in range(n):
        for j in range(p):
            if grid[i][j] == 1:
                res += helper(i, j)
    
    return res



if __name__ == "__main__":
    grid = [
        [0,1,1,0],
        [1,1,0,0],
        [0,1,0,0],
        [1,1,0,0]
        ]
    grid = [[1,0]]
    grid = [
        [1],
        [1],
        [1],
        [0],
        [1],
        [1]
        ]
    res = islandPerimeter(grid)
    print(res)
