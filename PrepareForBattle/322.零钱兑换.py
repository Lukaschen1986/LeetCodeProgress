# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:59:09 2021

@author: ASUS
"""
import time

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
                print(f"c {c} i {i} dp {dp}")
                time.sleep(2)
    
    if dp[-1] == float("inf"):
        return -1
    else:
        return dp[-1]
    

if __name__ == "__main__":
    coins = [11, 5, 1]
    amount = 15
