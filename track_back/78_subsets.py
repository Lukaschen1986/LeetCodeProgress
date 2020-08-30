# -*- coding: utf-8 -*-
# 解法一：借助 combinations
from itertools import combinations

def subsets(nums: list) -> list:
    res = []
    
    for i in range(len(nums)+1):
        combine = combinations(nums, i)
        for x in combine:
            res.append(list(x))
    
    return res
        

# 解法二：回溯法
def subsets(nums: list) -> list:
    res = []
    
    def track_back(combination, idx):
        if idx == len(nums):
            res.append(combination)
        else:
            track_back(combination, idx+1)
            track_back(combination + [nums[idx]], idx+1)
    
    track_back([], 0)
    return res


    
if __name__ == "__main__":
    nums = [1,2,3]
    nums = [1,9,8,3,-1,0]
    subsets(nums)
