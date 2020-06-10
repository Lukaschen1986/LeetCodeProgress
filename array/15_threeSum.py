# -*- coding: utf-8 -*-
def threeSum(nums: list) -> list:
    if len(nums) <= 2:
        return []
    
    nums.sort()
    res = []
    
    if nums[0] > 0:
        return []
    
    for k in range(0, len(nums)-2):
        if (k >= 1) and (nums[k] == nums[k-1]):
            continue
        
        i = k + 1
        j = len(nums) - 1
        
        while i < j:
            sum_ = nums[k] + nums[i] + nums[j]
            
            if sum_ == 0:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while (i < j) and (nums[i] == nums[i-1]):
                    i += 1
                while (i < j) and (nums[j] == nums[j+1]):
                    j -= 1
                
            elif sum_ < 0:
                i += 1
                while (i < j) and (nums[i] == nums[i-1]):
                    i += 1
                
            elif sum_ > 0:
                j -= 1
                while (i < j) and (nums[j] == nums[j+1]):
                    j -= 1
    
    return res
