# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:02:50 2021

@author: ASUS
"""

def searchMatrix(matrix, target) -> bool:
    """
    time = O(N)
    space = O(1)
    """
    n = len(matrix)
    p = len(matrix[0])
    i = 0
    j = p - 1
    
    while (i < n) and (j >= 0):
        if matrix[i][j] == target:
            return True
        elif target < matrix[i][j]:
            j -= 1
        elif target > matrix[i][j]:
            i += 1
            
    return False



if __name__ == "__main__":
    matrix = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
        ]
    target = 3
    searchMatrix(matrix, target)
