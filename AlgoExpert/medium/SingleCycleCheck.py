# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:08:09 2021

@author: ASUS
"""
def single_cycle_check(array: list) -> bool:
    """
    ​O(N) time | O(N) space
    """
    dp = [0]*len(array)
    i = 0
    
    while sum(dp) < len(array):
        dp[i] += 1
        i = get_next_i(i, array)
    
    if max(dp) == 1:
        return True
    else:
        return False
    
        
def get_next_i(i, array):
    i = (i + array[i]) % len(array)
    if i >= 0:
        return i
    else:
        return i + len(array)
    
    

if __name__ == "__main__":
    array = [2, 1, -3, 4, 5, -2]
    single_cycle_check(array)
    
