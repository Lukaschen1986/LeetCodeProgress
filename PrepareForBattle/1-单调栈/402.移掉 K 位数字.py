# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:53:25 2021

@author: ASUS
"""

def removeKdigits(num, k):
    lst = list(num)
    n = len(lst)
    stack = []    
    
    for i in range(n):
        while stack and (int(lst[i]) < int(lst[stack[-1]])) and (k > 0):
            idx = stack.pop()
            lst[idx] = ""
            k -= 1
        stack.append(i)
    
    lst = lst[0: n-k] # 很玄妙
    res = "".join(lst).lstrip("0")
    if res:
        return res
    else:
        return "0"


if __name__ == "__main__":
    num = "1432219"
    k = 3
    
    num = "12345264"
    k = 4
    
    num = "9"
    k = 1
    
    num = "112"
    k = 1

    removeKdigits(num, k)
