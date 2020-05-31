# -*- coding: utf-8 -*-
def twoSum(nums: int, target: int) -> int:
    dct = {v:k for (k,v) in enumerate(nums)}
    
    for i in range(len(nums)):
        resid = target - nums[i]
        if (resid in dct) and (i != dct[resid]):
            return [i, dct[resid]]
    
    return -1

if __name__ == "__main__":
    nums = [3, 3]
    target = 6
    twoSum(nums, target)
