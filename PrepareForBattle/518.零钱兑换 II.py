# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:01:05 2021

@author: ASUS
"""
import time

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
                print(f"c {c} i {i} dp {dp}")
                time.sleep(2)
                
    return dp[-1]

if __name__ == "__main__":
    coins = [11, 5, 1]
    amount = 15
