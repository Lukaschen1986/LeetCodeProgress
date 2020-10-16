# -*- coding: utf-8 -*-
def min_number_of_coins_for_change(coins: list, target: int) -> int:
    """
    最小硬币数量：给定硬币面值和目标金额，算出满足目标金额最少需要的硬币数量
    动规：O(N^2) time | O(N) space
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


if __name__ == "__main__":
    coins = [1, 2, 4]
    target = 6
    
    coins = [2, 4]
    target = 5
    
    min_number_of_coins_for_change(coins, target)
