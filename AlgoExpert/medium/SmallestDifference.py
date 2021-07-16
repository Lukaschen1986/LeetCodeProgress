# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 20:33:17 2021

@author: ASUS
"""
def smallest_difference(a: list, b: list) -> list:
    """
    ​O(NlogN) time | O(1) space
    """
    a.sort()
    b.sort()
    i = 0
    j = 0
    dct = {}
    
    while (i < len(a)) and (j < len(b)):
        diff = abs(a[i] - b[j])
        dct[diff] = [a[i], b[j]]
        
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            break
    
    return dct[min(dct)]
    

def smallest_difference(a: list, b: list) -> list:
    """
    ​O(NlogN) time | O(1) space
    """
    a.sort()
    b.sort()
    i = 0
    j = 0
    diff = float("inf")
    
    while (i < len(a)) and (j < len(b)):
        diff_run = abs(a[i] - b[j])
        if diff_run < diff:
            diff = diff_run
            res = [a[i], b[j]]
        
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            return [a[i], b[j]]
        
    return res
        

if __name__ == "__main__":
    a = [-1, 5, 10, 20, 28, 3]
    b = [26, 134, 20, 15, 17]
    smallest_difference(a, b)
