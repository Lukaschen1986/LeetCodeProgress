# -*- coding: utf-8 -*-
def combinationSum(candidates: list, target: int) -> list:
    res = []
    
    def track_back(combination, target):
        if (target == 0) and (sorted(combination) not in res):
            res.append(sorted(combination))
        else:
            for x in candidates:
                resid = target - x
                if resid >= 0:
                    track_back(combination + [x], resid)
                
    track_back([], target)
    return res
    
    
if __name__ == "__main__":
    candidates = [8,7,4,3]
    target = 11
    combinationSum(candidates, target)
