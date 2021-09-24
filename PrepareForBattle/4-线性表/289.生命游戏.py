# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 22:36:27 2021

@author: ASUS
"""

import copy

def gameOfLife(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    n = len(board)
    p = len(board[0])
    board_old = copy.deepcopy(board)

    def helper(i, j):
        count = 0
        direct = [(-1,0), (-1,1), (0,1), (1,1),
                  (1,0), (1,-1), (0,-1), (-1,-1)]
        for (x,y) in direct:
            if (0 <= i+x < n) and (0 <= j+y < p):
                count += board_old[i+x][j+y]
        return count

    for i in range(n):
        for j in range(p):
            count = helper(i, j)
            if board_old[i][j] == 1 and (count < 2 or count > 3):
                board[i][j] = 0
            if board_old[i][j] == 1 and count in [2,3]:
                board[i][j] = 1
            if board_old[i][j] == 0 and count == 3:
                board[i][j] = 1
        
        
if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
