# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:04:43 2021

@author: ASUS
"""
def letterCombinations(digits):
    if not digits:
        return []
    
    dct = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
        }
    res = []
    
    def back_track(combination, digits):
        if not digits:
            res.append(combination)
            return 
        else:
            lst = dct.get(digits[0])
            for x in lst:
                back_track(combination + x, digits[1:])
            
    back_track("", digits)
    return res
    
    
    
if __name__ == "__main__":
    digits = "23"
    letterCombinations(digits)
