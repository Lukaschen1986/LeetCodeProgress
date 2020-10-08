# -*- coding: utf-8 -*-
def min_number_of_coins_for_change(coins: list, target: int) -> int:
    """
    最小找零问题
    O(N^2) time | O(N) space
    """
    dct = {k:float("inf") for (k, _) in enumerate(range(target + 1))}
    dct[0] = 0
    
    for c in coins:
        for (k, _) in dct.items():
            if c <= k:
                dp = k - c
                dct[k] = min(dct.get(k), 1 + dct.get(dp))
    
    if dct.get(target) == float("inf"):
        return -1
    else:
        return dct.get(target)

    

def all_cases(coins, target):
    """
    返回所有可能的硬币组合（回溯）
    """
    res = []
    constant = target
    
    def trace_back(combination, target):
        if target <= 0:
            if (sum(combination) == constant) and (sorted(combination) not in res):
                res.append(combination)
                return
        else:
            for coin in coins:
                resid = target - coin
                trace_back(combination + [coin], resid)
    
    trace_back([], target)
    return res


if __name__ == "__main__":
    coins = [1, 2, 4]
    target = 6
    
    coins = [2, 4]
    target = 5
    
    min_number_of_coins_for_change(coins, target)
    all_cases(coins, target)
