# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:12:23 2021

@author: ASUS
"""

def longestPalindrome(s):
    interval_global = [0, 0]
    
    for i in range(len(s)):
        interval_even = helper(s, i, i+1)
        interval_odd = helper(s, i-1, i+1)
        interval_local = max(interval_even, interval_odd, key=lambda x: x[1] - x[0])
        interval_global = max(interval_global, interval_local, key=lambda x: x[1] - x[0])
    
    return s[interval_global[0]: interval_global[1]]


def helper(s, i, j):
    while (i >= 0) and (j < len(s)):
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            break
    
    return [i+1, j]
    
    
if __name__ == "__main__":
    s = "babad"
