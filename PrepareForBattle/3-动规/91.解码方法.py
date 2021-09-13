# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:59:08 2021

@author: ASUS
"""

def numDecodings(s):
    dct = {str(i):1 for i in range(1,10)}
    def helper(s, memory=dct):
        if not s:
            return 1
        elif s.startswith("0"):
            return 0
        elif s in memory:
            return memory.get(s)
        elif s[0:2] > "26":
            memory[s] = helper(s[1:])
            return memory.get(s)
        else:
            memory[s] = helper(s[1:]) + helper(s[2:])
            return memory.get(s)
    
    res = helper(s, memory=dct)
    return res



if __name__ == "__main__":
    s = "102713"
    s = "102213"
    s = "0"
    s = "111111111111111111111111111111111111111111111"
    s = "276"
    numDecodings(s)
