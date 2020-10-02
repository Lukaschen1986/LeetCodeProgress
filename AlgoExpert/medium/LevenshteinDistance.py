# -*- coding: utf-8 -*-
def levenshtein_distance(str1, str2):
    """
    字符串编辑距离
    # O(N^2) time | O(N^2) space
    """
    # 构造0矩阵
    dp = [[0]*(len(str2)+1) for i in range(len(str1)+1)]
    # 第一行赋值
    dp[0] = [j for j in range(len(str2)+1)]
    # 第一列赋值
    for i in range(len(str1)+1):
        dp[i][0] = i
    '''
    构造完后形如：
    [
     [0, 1, 2, 3, 4], 
     [1, 0, 0, 0, 0], 
     [2, 0, 0, 0, 0], 
     [3, 0, 0, 0, 0]
     ]
    '''
    # 动规
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[-1][-1]
    


if __name__ == "__main__":
    str1 = "abc"
    str2 = "yabd"
    levenshtein_distance(str1, str2)
