# -*- coding: utf-8 -*-
def maxArea(height: list) -> int:
    n = len(height)
    i = 0
    j = n - 1
    area = 0
    
    while i < j:
        w = j - i
        h = min(height[i], height[j])
        area = max(area, w*h)
        
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    
    return area
