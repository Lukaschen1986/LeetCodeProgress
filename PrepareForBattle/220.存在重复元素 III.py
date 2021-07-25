# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:14:15 2021

@author: ASUS
"""

def containsNearbyAlmostDuplicate(nums: list, k: int, t: int) -> bool:
    """
    ​O(N) time | O(1) space
    """
    dct = {}
    for i in range(len(nums)):
        idx = nums[i] // (t + 1)
        if idx in dct:
            return True
        elif (idx-1 in dct) and (abs(nums[i]-dct[idx-1]) <= t):
            return True
        elif (idx+1 in dct) and (abs(nums[i]-dct[idx+1]) <= t):
            return True
        dct[idx] = nums[i]
        
        if i >= k:
            idx_drop = nums[i-k] // (t + 1)
            del dct[idx_drop]
    
    return False

    
    
if __name__ == "__main__":
    nums = [1,2,3,1]
    t = 0
    k = 3
    containsNearbyAlmostDuplicate(nums, k, t)
    
    nums = [1,5,9,1,5,9]
    t = 3
    k = 2
    containsNearbyAlmostDuplicate(nums, k, t)
