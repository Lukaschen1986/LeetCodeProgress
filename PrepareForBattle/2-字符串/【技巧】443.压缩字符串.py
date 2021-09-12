# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:54:10 2021

@author: ASUS
"""

def compress(chars):
    """
    time = O(N)
    space = O(1)
    """
    n = len(chars)
    i, count = 0, 1
    
    for j in range(1, n+1):
        if (j < n) and (chars[j] == chars[j-1]):
            count += 1
        else:
            chars[i] = chars[j-1] # 神来之笔
            i += 1 # 神来之笔
            if count > 1:
                for k in str(count):
                    chars[i] = k
                    i += 1
            count = 1
                
    return i

        

if __name__ == "__main__":
    chars = ["a", "a", "a", "b", "b", "a", "a"]
    chars = ["a"]
