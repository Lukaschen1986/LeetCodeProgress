# -*- coding: utf-8 -*-
from collections import Counter
import numpy as np

def isValidSudoku(board: list) -> bool:
    m = np.array(board)
    
    # 判断行
    for i in range(len(m)):
        lst = list(m[i])
        dct = Counter(lst)
        for (k,v) in dct.items():
            if (v > 1) and (k != "."):
                return False
    
    # 判断列
    for j in range(len(m)):
        lst = list(m[:,j])
        dct = Counter(lst)
        for (k,v) in dct.items():
            if (v > 1) and (k != "."):
                return False
    
    # 判断方块
    row = 0
    while row < 9:
        for col in [0, 3, 6]:
            lst = list(m[0+row:3+row, 0+col:3+col].reshape(1, -1)[0])
            dct = Counter(lst)
            for (k,v) in dct.items():
                if (v > 1) and (k != "."):
                    return False
        row += 3
        
    return True


if __name__ == "__main__":
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]
    isValidSudoku(board)
