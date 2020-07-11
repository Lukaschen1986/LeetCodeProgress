# -*- coding: utf-8 -*-
def searchInsert(nums: list, target: int) -> int:
    """
    顺序查找
    """
    if target in nums:
        return nums.index(target)
    else:
        for i in range(len(nums)):
            if target < nums[i]:
                return i
    
    return len(nums)
    
def searchInsert(nums: list, target: int) -> int:
    """
    二分查找
    """
    if target in nums:
        return nums.index(target)
    elif target > max(nums):
        return len(nums)
    else:
        a = 0
        b = len(nums) - 1
        
        while a < b:
            mid = (a + b) // 2
            if target < nums[mid]:
                b = mid
            else:
                a = mid + 1
        
        return a
        
        
if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2
    
    nums = [1,3,5,6]
    target = 7
    
    nums = [1,3,5,6,9,12]
    target = 14
