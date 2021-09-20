# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:15:54 2021

@author: ASUS
"""

def findMissingRanges(nums, lower, upper):
    upper += 1
    nums = nums + [lower] + [upper]
    nums.sort()
    l = nums.index(lower)
    r = nums.index(upper)
    nums = nums[l:r+1]
    n = len(nums)
    res = []
    
    for i in range(n-1):
        j = i + 1
        if nums[j] - nums[i] <= 1:
            continue
        elif nums[j] - nums[i] == 2:
            miss = str(nums[i]+1)
            res.append(miss)
        else:
            miss = str(nums[i]+1) + "->" + str(nums[j]-1)
            res.append(miss)
            
    return res
    
    
if __name__ == "__main__":
    nums = [0, 2, 4, 6, 50, 75]
    nums = [0, 2]
    lower = 1
    upper = 99
    findMissingRanges(nums, lower, upper)
