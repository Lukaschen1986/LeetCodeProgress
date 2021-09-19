# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 14:59:46 2021

@author: ASUS
"""

def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    time = O(N^2)
    space = O(N^2)
    """
    n = len(text1)
    m = len(text2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[j-1] == text2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
