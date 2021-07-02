# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:25:13 2021

@author: ASUS
"""
def min_number_of_coins_for_change(lst: list, target: int) -> int:
    """
    最小找零问题
    ​O(N^2) time | O(N) space
    """
    dp = [float("inf")] * (target + 1)
    dp[0] = 0
    
    for x in lst:
        for i in range(1, len(dp)):
            if x <= i:
                dp[i] = min(dp[i], 1 + dp[i-x])
    
    return dp[-1]
    
    
    
if __name__ == "__main__":
    lst = [2, 1, 4]
    target = 6
    min_number_of_coins_for_change(lst, target)
