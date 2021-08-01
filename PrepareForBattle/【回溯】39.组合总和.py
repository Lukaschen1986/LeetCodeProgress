# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:25:50 2021

@author: ASUS
"""
def combinationSum(candidates, target):
    res = []
    
    def back_track(combination, target):
        if (target == 0) and (sorted(combination) not in res):
            res.append(sorted(combination))
            return 
        else:
            for x in candidates:
                resid = target - x
                if resid >= 0:
                    back_track(combination + [x], resid)
    
    back_track([], target)
    return res
    

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    combinationSum(candidates, target)
