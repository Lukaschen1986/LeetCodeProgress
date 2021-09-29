# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:23:57 2021

@author: ASUS
"""

def lengthOfLongestSubstringTwoDistinct(s):
    """
    time = O(N)
    space = O(1)
    """
    n = len(s)
    i = j = 0
    res = 0
    
    while (j < n) and (i <= j):
        tmp = s[i:j+1]
        count = len(set(tmp))
        if count <= 2:
            res = max(res, len(tmp))
            j += 1
        else:
            i += 1
    
    return res


if __name__ == "__main__":
    s = "ccbbaaa"
    s = "eveba"
    res = lengthOfLongestSubstringTwoDistinct(s)
    print(res)
