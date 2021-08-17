# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:04:43 2021

@author: ASUS
"""
def letterCombinations(digits):
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
    if not digits:
        return []
    res = []
    
    def back_track(combination, digits):
        if not digits:
            res.append(combination)
        else:
            k = digits[0]
            lst = dct.get(k)
            for s in lst:
                back_track(combination + s, digits[1:])
    
    back_track("", digits)
    return res
    
    
    
if __name__ == "__main__":
    digits = "23"
    letterCombinations(digits)
