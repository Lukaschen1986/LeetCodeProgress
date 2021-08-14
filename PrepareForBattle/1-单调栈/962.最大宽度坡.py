# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 11:46:31 2021

@author: ASUS
"""

def maxWidthRamp(nums):
    # 单调递减栈
    n = len(nums)
    stack = []    
    for i in range(n):
        while (not stack) or (nums[i] < nums[stack[-1]]):
            stack.append(i)
    
    # 从后向前遍历
    res = 0
    for j in range(n-1, -1, -1):
        print(j)
        while stack and (nums[j] >= nums[stack[-1]]):
            idx = stack.pop()
            res = max(res, j - idx)
            
    return res


if __name__ == "__main__":
    nums = [6,2,8,2,1,5]
    nums = [9,8,1,0,1,9,4,0,4,1]
    nums = [2,2,1]
    maxWidthRamp(nums)
