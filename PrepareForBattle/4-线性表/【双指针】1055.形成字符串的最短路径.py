# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:29:08 2021

@author: ASUS
"""

def shortestway(source, target):
    """
    time = O(N*M)
    space = O(N)
    """
    n = len(source)
    m = len(target)
    for i in range(m):
        if target[i] not in source:
            return -1
    
    i = 0
    j = 0
    res = []
    tmp = ""
    
    def helper(j, tmp):
        if j == n-1:
            j = 0
            res.append(tmp)
            tmp = ""
        else:
            j += 1
        return j, tmp
    
    while i < m:
        if target[i] == source[j]:
            tmp += source[j]
            i += 1
            j, tmp = helper(j, tmp)
        else:
            j, tmp = helper(j, tmp)
            
    return len(res)
    



if __name__ == "__main__":
    source = "xyz"
    target = "xzyxz"
    
    source = "abc"
    target = "acdbc"
    
    source = "abc"
    target = "abcbc"
    
    shortestway(source, target)
