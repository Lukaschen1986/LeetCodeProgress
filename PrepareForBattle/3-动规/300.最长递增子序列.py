# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 20:19:36 2021

@author: ASUS
"""
def lengthOfLIS(nums):
    """
    time = O(N^2)
    space = O(N)
    """
    n = len(nums)
    dp = [1]*n
    
    for i in range(1, n):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)
    
    
if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101]
    nums = [0,1,0,3,2,3]
