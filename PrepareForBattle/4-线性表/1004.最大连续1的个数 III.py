# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:30:20 2021

@author: ASUS
"""

from collections import deque

def longestOnes(nums, k) -> int:
    # 特例
    if k == 0:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            if (nums[i] == 1) and (nums[i-1] == 0):
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)
            
    if k == len(nums):
        return len(nums)
    
    # 常规
    n = len(nums)
    i = 0
    max_len = 0
    queue = deque([])
    
    for j in range(n):
        if k > 0:
            if nums[j] == 0:
                k -= 1
                queue.append(j)
            max_len = max(max_len, j-i+1)
                
        else:
            if nums[j] == 0:
                node = queue.popleft()
                i = node + 1
                queue.append(j)
            max_len = max(max_len, j-i+1)
    
    return max_len



if __name__ == "__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 1
    
    nums = [0,0,1,1,1,0,0]
    k = 4
    
    nums = [1,1,1,1,1]
