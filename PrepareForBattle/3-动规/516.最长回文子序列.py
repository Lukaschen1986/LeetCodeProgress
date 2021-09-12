# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:43:34 2021

@author: ASUS
"""

def longestPalindromeSubseq(s: str) -> int:
    """
    time = O(N^2)
    space = O(N^2)
    """
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    
    for i in range(n-1, -1, -1): # 神来之笔
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2 # 神来之笔
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1]) # 神来之笔
    
    return dp[0][-1]


if __name__ == "__main__":
    s = "cbbd"
