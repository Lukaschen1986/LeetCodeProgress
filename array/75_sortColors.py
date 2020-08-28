# -*- coding: utf-8 -*-
def sortColors(nums: list) -> None:
    i = 0
    k = 0
    j = len(nums) - 1

    while i <= j:
        if nums[i] == 0:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k += 1
        elif nums[i] == 1:
            i += 1
        elif nums[i] == 2:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1

    
if __name__ == "__main__":
    nums = [1,0,2,1,1,0]
    nums = [2,0,1]
    sortColors(nums)
