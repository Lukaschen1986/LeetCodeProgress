# -*- coding: utf-8 -*-
def number_of_ways_to_make_change(coins: list, target: int) -> int:
    """
    找零组合：给定硬币面值和目标金额，算出达到目标金额所有的零钱组合种类
    动规：O(N^2) time | O(N) space
    """
    dct = {k:0 for (k,_) in enumerate(range(target + 1))}
    dct[0] = 1
    
    for c in coins:
        for (k,_) in dct.items():
            if c <= k:
                dp = k - c
                dct[k] += dct.get(dp)
    
    return dct.get(target)
    
    
def number_of_ways_to_make_change(coins: list, target: int) -> int:
    """
    找零组合：给定硬币面值和目标金额，算出达到目标金额所有的零钱组合种类
    回溯：O(N!) time | O(N) space
    """
    res = []
    constant = target
    
    def trace_back(combination, target):
        if target <= 0:
            if (sum(combination) == constant) and (sorted(combination) not in res):
                res.append(combination)
                return 
        else:
            for c in coins:
                resid = target - c
                trace_back(combination + [c], resid)
        
    trace_back([], target)
    return len(res)
        

if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    target = 10
    number_of_ways_to_make_change(coins, target)
