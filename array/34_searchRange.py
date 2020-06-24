# -*- coding: utf-8 -*-
def searchRange(nums: list, target: int) -> list:
    if target not in nums:
        return [-1, -1]
    
    left = nums.index(target)
    if target not in nums[left+1:]:
        return [left, left]
    else:
        a = left + 1
        b = len(nums) - 1
        
        while a < b:
            mid = (a + b) // 2
            if target < nums[mid]:
                b = mid
            else:
                a = mid + 1
        
        if target == nums[b]:
            return [left, b]
        else:
            return [left, b-1]
