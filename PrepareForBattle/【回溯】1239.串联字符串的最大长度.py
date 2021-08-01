# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:29:02 2021

@author: ASUS
"""
def power_set(lst):
    """
    lst = [1, 2, 3]
    """
    res = [[]]
    
    for x in lst:
        for i in range(len(res)):
            val = res[i] + [x]
            res.append(val)
    
    return res



def maxLength(arr):
    res = [""]
    
    for s in arr:
        for i in range(len(res)):
            inter = set(s).intersection(set(res[i]))
            equal = (len(set(s)) == len(s))
            if (not inter) and equal:
                val = res[i] + s
                res.append(val)
    
    return max(len(lst) for lst in res)
    

if __name__ == "__main__":
    arr = ["un","iq","ue"]
    maxLength(arr)
