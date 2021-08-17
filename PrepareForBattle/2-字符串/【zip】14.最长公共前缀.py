# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 20:54:17 2021

@author: ASUS
"""

def longestCommonPrefix(strs):
    iters = zip(*strs)
    idx = 0
    
    for tpl in iters:
        if len(set(tpl)) == 1:
            idx += 1
        else:
            break
    
    return strs[0][0:idx]
    
    
    
    
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    longestCommonPrefix(strs)
    
