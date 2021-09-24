# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:25:11 2021

@author: ASUS
"""

def lenLongestFibSubseq(arr) -> int:
    """
    time = O(N^3)
    space = O(1)
    """
    n = len(arr)
    s = set(arr)
    res = 0

    for i in range(0, n-1):
        for j in range(i+1, n):
            count = 2
            a, b = arr[i], arr[j]
            c = a + b
            while c in s:
                count += 1
                a, b = b, c
                c = a + b
            res = max(res, count)
    
    if res <= 2:
        return 0
    else:
        return res


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    arr = [1,3,7,11,12,14,18]
