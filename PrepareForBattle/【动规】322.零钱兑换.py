# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 17:17:40 2021

@author: ASUS
"""
def coinChange(coins, amount):
    """
    最少的硬币个数
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    
    for c in coins:
        for i in range(1, len(dp)):
            if c <= i:
                dp[i] = min(dp[i], 1 + dp[i-c])
    return dp[-1]
    

if __name__ == "__main__":
    coins = [11, 5, 1]
    amount = 15
