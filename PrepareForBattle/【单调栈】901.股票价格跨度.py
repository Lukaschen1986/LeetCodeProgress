# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:02:54 2021

@author: ASUS
"""

def func(price):
    n = len(price)
    res = [1] * len(price)    
    stack = []
    
    for i in range(n):
        while stack and (price[i] >= price[stack[-1]]):
            idx = stack.pop()
            res[i] += res[idx]
        
        stack.append(i)
                
    return res


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and (price >= self.stack[-1][1]):
            idx, val = self.stack.pop()
            res += idx
        
        self.stack.append([res, price])
        return res


if __name__ == "__main__":
    price = [100, 80, 60, 70, 60, 75, 85]
    
