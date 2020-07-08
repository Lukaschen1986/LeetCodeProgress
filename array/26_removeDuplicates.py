# -*- coding: utf-8 -*-
def removeDuplicates(nums: list) -> int:
    for i in range(len(nums)-2, -1, -1):
        if nums[i] == nums[i+1]:
            # nums.remove(nums[i])
            del nums[i]
    
    return nums


if __name__ == "__main__":
    removeDuplicates(nums)
    nums = [1,1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
