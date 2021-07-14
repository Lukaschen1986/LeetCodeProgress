# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:54:42 2021

@author: ASUS
"""
def search_in_sorted_matrix(matrix: list, target: int) -> list:
    """
    ​O(N) time | O(1) space
    """
    for i in range(len(matrix)):
        if target in matrix[i]:
            j = matrix[i].index(target)
            return [i, j]
        else:
            continue
            
    return [-1, -1]


def search_in_sorted_matrix(matrix: list, target: int) -> list:
    """
    ​O(N) time | O(1) space
    """
    i = 0
    j = len(matrix[0]) - 1
    
    while (i < len(matrix)) and (j >= 0):
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            return [i, j]
    
    return [-1, -1]



if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]
    target = 44
    search_in_sorted_matrix(matrix, target)
