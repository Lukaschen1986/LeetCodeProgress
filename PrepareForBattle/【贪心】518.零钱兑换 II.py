# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 17:13:51 2021

@author: ASUS
"""
def coinChange(coins, amount):
    """
    硬币组合数
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for c in coins:
        for i in range(1, len(dp)):
            if c <= i:
                dp[i] = dp[i] + dp[i-c]
    
    return dp[-1]
    
    
if __name__ == "__main__":
    coins = [11, 5, 1]
    amount = 15
