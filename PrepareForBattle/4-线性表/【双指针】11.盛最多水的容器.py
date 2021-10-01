# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:47:05 2021

@author: ASUS
"""

def maxArea(height) -> int:
    """
    time = O(N)
    space = O(1)
    """
    n = len(height)
    i = 0
    j = n - 1
    res = 0

    while i < j:
        h = min(height[i], height[j])
        w = j - i
        area = h*w
        res = max(res, area)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    
    return res


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    res = maxArea(height)
    print(res)
