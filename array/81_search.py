# -*- coding: utf-8 -*-
def search(nums: list, target: int) -> bool:
    if target in nums:
        return True
    else:
        return False

    
if __name__ == "__main__":
    nums = [2,5,6,0,0,1,2]
    target = 0
    search(nums, target)
