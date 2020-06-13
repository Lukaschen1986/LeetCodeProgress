# -*- coding: utf-8 -*-
def threeSumClosest(nums: list, target: int) -> int:
    nums.sort()
    res = {}
    
    for k in range(0, len(nums)-2):
        i = k + 1
        j = len(nums) - 1
        
        while i < j:
            sum_ = nums[k] + nums[i] + nums[j]
            resid = abs(sum_ - target)
            
            if resid == 0:
                # return sum_
                pass
            elif sum_ < target:
                i += 1
            else:
                j -= 1
            
            res[resid] = sum_
    
    return res.get(min(res))
            

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    nums = [0, 2, 1, -3]
    target = 1
    threeSumClosest(nums, target)
