# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:54:42 2021

@author: ASUS
"""
def searchMatrix(matrix, target):
    i = 0
    j = len(matrix[0]) - 1    
    
    while (i < len(matrix)) and (j >= 0):
        if target < matrix[i][j]:
            j -= 1
        elif target > matrix[i][j]:
            i += 1
        else:
            return True
    
    return False
        
if __name__ == "__main__":
    matrix = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
        ]
    target = 5
    searchMatrix(matrix, target)
