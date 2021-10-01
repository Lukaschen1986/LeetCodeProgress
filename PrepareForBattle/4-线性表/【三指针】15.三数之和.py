# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:12:20 2021

@author: ASUS
"""

def threeSum(nums):
    # 特例
    if not nums:
        return []
    n = len(nums)
    if n <= 2:
        return []
    if (n == 3) and sum(nums) != 0:
        return []

    # 常规
    nums.sort()
    res = []

    for k in range(n-2):
        i = k + 1
        j = n - 1
        while i < j:
            target = nums[k] + nums[i] + nums[j]
            lst = [nums[k], nums[i], nums[j]]
            if target == 0:
                if sorted(lst) not in res:
                    res.append(lst)
                i += 1
                j -= 1
            elif target < 0:
                i += 1
            elif target > 0:
                j -= 1
                
                
    return res


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    res = threeSum(nums)
    print(res)
    k = 1
    i = 4
    j = 3
