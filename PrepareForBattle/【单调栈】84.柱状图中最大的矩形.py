# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 21:02:16 2021

@author: ASUS
"""

def largestRectangleArea(heights):
    heights = [0] + heights + [0]
    area = 0    
    stack = []    

    for i in range(len(heights)):
        while stack and (heights[i] < heights[stack[-1]]):
            idx = stack.pop()
            h = heights[idx]
            w = i - stack[-1] - 1
            area = max(area, w*h)
            
        stack.append(i)
        
    return area
        
        
        
if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    largestRectangleArea(heights)
    
