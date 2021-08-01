# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:40:21 2021

@author: ASUS
"""
def maxSubArray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    
    return max(dp)
        
    
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
