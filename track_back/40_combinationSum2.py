# -*- coding: utf-8 -*-
def combinationSum2(candidates: list, target: int) -> list:
    res = []
    candidates.sort()
    
    def track_back(combination, target, candidates):
        if (target == 0) and (sorted(combination) not in res):
            res.append(sorted(combination))
        else:
            for x in candidates:
                resid = target - x
                if resid >= 0:
                    candidates = candidates[1:] # 注：这一步不能写到track_back函数中
                    track_back(combination + [x], resid, candidates)
                
    track_back([], target, candidates)
    return res
    
    
if __name__ == "__main__":
    candidates = [1, 2]
    target = 4
    candidates = [2,5,2,1,2]
    target = 5
    combinationSum2(candidates, target)
