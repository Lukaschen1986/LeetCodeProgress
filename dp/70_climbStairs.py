# -*- coding: utf-8 -*-
def climbStairs(n: int) -> int:
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
    
    return dp[-1]

    
if __name__ == "__main__":
    n = 0
    n = 1
    n = 2
    n = 3
    n = 4
    climbStairs(n)
