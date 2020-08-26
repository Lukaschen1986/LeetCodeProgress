# -*- coding: utf-8 -*-
def searchMatrix(matrix: list, target: int) -> bool:
    if (not matrix) or (not matrix[0]):
        return False
    else:
        _min = matrix[0][0]
        _max = matrix[len(matrix)-1][-1]
        if (target < _min) or (target > _max):
            return False
        
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
    
    return False

    
if __name__ == "__main__":
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    searchMatrix(matrix, target)
