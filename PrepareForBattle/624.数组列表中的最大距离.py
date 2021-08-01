# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:19:19 2021

@author: ASUS
"""
def maxDistance(nums):
    nums.sort()
    min_val = nums[0][0]
    res = float("-inf")
    
    for lst in nums[1:]:
        max_val = lst[-1]
        res = max(res, abs(max_val - min_val))
    
    return res
    
    
if __name__ == "__main__":
    nums = [[1,2,3],[4,5],[1,2,3]]
