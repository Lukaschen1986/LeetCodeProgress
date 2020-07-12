# -*- coding: utf-8 -*-
def rotate(matrix: list) -> None:
    # 转置
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # 换列
    a = 0
    b = len(matrix) - 1
    while a < b:
        for k in range(len(matrix)):
            matrix[k][a], matrix[k][b] = matrix[k][b], matrix[k][a]
        a += 1
        b -= 1
    

if __name__ == "__main__":
    matrix = [
              [1,2,3],
              [4,5,6],
              [7,8,9]
            ]
    rotate(matrix)
