# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:21:48 2021

@author: ASUS
"""

def nextPermutation(nums) -> None:
    """
    time = O(N)
    space = O(1)
    """
    # 特例
    if len(nums) == 1:
        return nums
    if nums == sorted(nums, reverse=True):
        return nums.sort()

    # 常规
    n = len(nums)
    for i in range(n-2, -1, -1): # 神来之笔
        if nums[i] < nums[i+1]:
            break
    
    for j in range(n-1, i, -1):  # 神来之笔
        if nums[j] > nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = sorted(nums[i+1:])
            break
    
    return nums
    


if __name__ == "__main__":
    nums = [1, 2, 5, 8, 7]
    nums = [1, 2, 7, 5, 8]
    
    
    nums = [1, 2, 5, 7, 8]
    nums = [4,2,0,2,3,2,0]
    
    nums = [4,2,0,3,0,2,2]
    nums = [4,2,2,0,0,2,3]
    
    nextPermutation(nums)
