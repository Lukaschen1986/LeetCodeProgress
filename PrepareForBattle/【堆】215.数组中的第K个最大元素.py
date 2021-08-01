# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 15:29:08 2021

@author: ASUS
"""
def findKthLargest(nums: list, k: int) -> int:
    nums.sort(reverse=True)
    return nums[k-1]
    
    
    
if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    
    nums = [3,2,1,5,6,4]
    k = 2
    
    nums = [1]
    k = 1    
    
    findKthLargest(nums, k)
