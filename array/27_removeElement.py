# -*- coding: utf-8 -*-
def removeElement(nums: list, val: int) -> int:
    if val not in nums:
        return len(nums)
    else:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                # nums.remove(nums[i])
                del nums[i]
    
    return len(nums)
    
    
if __name__ == "__main__":
    removeElement(nums, val)
    nums = [0,1,2,2,3,0,4,2]
    val = 2
