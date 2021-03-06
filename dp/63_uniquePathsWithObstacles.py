# -*- coding: utf-8 -*-
def uniquePathsWithObstacles(obstacleGrid: list) -> int:
    dp = obstacleGrid[:]
    m = len(dp)
    n = len(dp[0])
    
    if dp[0][0] == 1:
        return 0
    else:
        dp[0][0] = 1
    
    for i in range(1, m):
        if dp[i][0] == 1:
            dp[i][0] = 0
        else:
            dp[i][0] = dp[i-1][0]
    
    for j in range(1, n):
        if dp[0][j] == 1:
            dp[0][j] = 0
        else:
            dp[0][j] = dp[0][j-1]
    
    for i in range(1, m):
        for j in range(1, n):
            if dp[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[-1][-1]



if __name__ == "__main__":
    obstacleGrid = [
                      [0,0,0],
                      [0,1,0],
                      [0,0,0]
                    ]
    uniquePathsWithObstacles(obstacleGrid)
