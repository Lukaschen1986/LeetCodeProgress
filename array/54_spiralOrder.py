# -*- coding: utf-8 -*-
import numpy as np


def spiralOrder(matrix: list) -> list:
    res = []
    Matrix = np.array(matrix, dtype=np.int64)
    
    while Matrix.any():
        N, p = Matrix.shape
        
        if (N == 1) and (p >= 1):
            res.extend(Matrix[0].tolist())
        elif (N > 1) and (p == 1):
            res.extend(Matrix[:,0].tolist())
        else:
            res.extend(Matrix[0, 0:-1].tolist())
            res.extend(Matrix[0:-1, -1].tolist())
            res.extend(Matrix[-1, -1:0:-1].tolist())
            res.extend(Matrix[-1:0:-1, 0].tolist())
        
        Matrix = Matrix[1:-1, 1:-1]

    return res


if __name__ == "__main__":
    matrix = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]
    matrix = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12],
          [13,14,15,16]
        ]
    matrix = [
          [1, 2, 3],
          [5, 6, 7],
          [9,10,11],
          [13,14,15]
        ]
    matrix = [[7],[9],[6]]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    
    spiralOrder(matrix)
