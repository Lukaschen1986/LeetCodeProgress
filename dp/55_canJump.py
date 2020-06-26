# -*- coding: utf-8 -*-
def canJump(nums: list) -> bool:
    bound = len(nums) - 1
    
    for i in range(len(nums)-2, -1, -1):
        if nums[i] >= bound - i:
            bound = i
            
    return bound == 0



if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
