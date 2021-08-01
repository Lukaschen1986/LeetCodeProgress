# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:20:08 2021

@author: ASUS
"""
def generateParenthesis(n):
    m = n*2
    left = 0
    right = 0    
    res = []    
    
    def back_track(combination, left, right):
        if len(combination) == m:
            res.append(combination)
            return
        else:
            if left < n:
                back_track(combination + "(", left+1, right)
            if right < left:
                back_track(combination + ")", left, right+1)
    
    back_track("", left, right)
    return res
    
if __name__ == "__main__":
    n = 2
    generateParenthesis(n)
