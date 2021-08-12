# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:26:32 2021

@author: ASUS
"""

def nextGreaterElements(nums):
    stack = []
    n = len(nums)
    res = [-1] * n
    
    for i in range(n*2 - 1):
        while stack and (nums[i % n] > nums[stack[-1]]):
            idx = stack.pop()
            res[idx] = nums[i % n]
        
        stack.append(i % n)
    
    return res


if __name__ == "__main__":
    nums = [1,2,1]
    
    
