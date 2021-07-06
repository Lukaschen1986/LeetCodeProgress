# -*- coding: utf-8 -*-
def power_set(nums):
    """
    输出列表的所有子集
    # O(n*2^n) time | O(n*2^n) space
    """
    res = [[]]
    
    for x in lst:
        for i in range(len(res)):
            res.append(res[i] + [x])
    
    return res


from itertools import combinations
def power_set(nums):
    res = []
    
    for choose in range(len(nums) + 1):
        for com in combinations(nums, choose):
            val = list(com)
            res.append(val)
    
    return res
        

if __name__ == "__main__":
    nums = [1, 2, 3]
    power_set(nums)
