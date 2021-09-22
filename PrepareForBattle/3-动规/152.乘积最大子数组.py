# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:17:05 2021

@author: ASUS
"""

def maxProduct(nums) -> int:
    """
    time = O(N)
    space = O(N)
    """
    n = len(nums)
    dp_max = [0]*n
    dp_min = [0]*n
    dp_max[0] = nums[0]
    dp_min[0] = nums[0]
    
    for i in range(1, n):
        if nums[i] < 0: # 神来之笔
            dp_max[i-1], dp_min[i-1] = dp_min[i-1], dp_max[i-1]
        dp_max[i] = max(nums[i], nums[i]*dp_max[i-1])
        dp_min[i] = min(nums[i], nums[i]*dp_min[i-1])
    
    return max(max(dp_max), max(dp_min)) # 神来之笔


    
if __name__ == "__main__":
    nums = [2, 3, -2, 4, 2]
    nums = [-2,0,-1]
    nums = [2,3,-2,4]
