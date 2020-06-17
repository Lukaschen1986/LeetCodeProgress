# -*- coding: utf-8 -*-
def nextPermutation(nums: list) -> list:
    n = len(nums)
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            nums[i+1:] = sorted(nums[i+1:])
            
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    break
            
            nums[i], nums[j] = nums[j], nums[i]
            return nums
    
    nums.sort()
    return nums
