# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:18:27 2021

@author: ASUS
"""

def countSubstrings(s):
    res = []
    
    for i in range(len(s)):
        s_even = helper(s, i, i+1)
        s_odd = helper(s, i, i)
        res.extend(s_even)
        res.extend(s_odd)
    

def helper(s, i, j):
    local = []
    while (i >= 0) and (j < len(s)):
        if s[i] == s[j]:
            local.append(s[i: j+1])
            i -= 1
            j += 1
        else:
            break
    
    return local
    
    
if __name__ == "__main__":
    s = "aaabcb"
    
    
