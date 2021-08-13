# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:45:53 2021

@author: ASUS
"""

def trap(height):
    n = len(height)
    res = 0
    stack = []

    for i in range(n):
        while stack and (height[i] > height[stack[-1]]):
            idx = stack.pop()
            if not stack:
                continue
                
            w = i - stack[-1] - 1
            h = min(height[stack[-1]], height[i]) - height[idx]
            res += w*h
        
        stack.append(i)
    
    return res


if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    trap(height)
    
