# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:32:53 2021

@author: ASUS
"""
def permute(nums):
    res = []
    
    def back_track(combination, nums):
        if not nums:
            res.append(combination)
            return 
        else:
            for i in range(len(nums)):
                back_track(combination + [nums[i]], nums[0:i] + nums[i+1:])
    
    back_track([], nums)
    return res
    
    
if __name__ == "__main__":
    nums = [1,2,3]
    permute(nums)
