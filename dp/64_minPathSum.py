# -*- coding: utf-8 -*-
def minPathSum(grid: list) -> int:
    N = len(grid)
    p = len(grid[0])
    dp = [[0]*p for _ in range(N)]
    dp[0][0] = grid[0][0]
    
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    for j in range(1, p):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    for i in range(1, N):
        for j in range(1, p):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]
    
    
if __name__ == "__main__":
    grid = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    minPathSum(grid)
