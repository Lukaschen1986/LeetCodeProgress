# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:17:28 2021

@author: ASUS
"""

def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []    
    
    for i in range(len(temperatures)):
        while stack and (temperatures[i] > temperatures[stack[-1]]):
            idx = stack.pop()
            res[idx] = i - idx
        
        stack.append(i)
    
    return res


if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    dailyTemperatures(temperatures)
    
