# -*- coding: utf-8 -*-
# import time

def fourSum(nums: list, target: int) -> list:
    if len(nums) < 4:
        return []
    
    res = []
    nums.sort()
    
    for a in range(0, len(nums)-3):
        if (a >= 1) and (nums[a] == nums[a-1]):
            continue
        
        for b in range(a+1, len(nums)-2):
            if (b >= a+2) and (nums[b] == nums[b-1]):
                continue
            
            c = b + 1
            d = len(nums) - 1
            
            while c < d:
                lst = [nums[a], nums[b], nums[c], nums[d]]
                
                if (sum(lst) == target):
                    res.append(lst)
                    c += 1
                    d -= 1
                    while (c < d) and (nums[c] == nums[c-1]):
                        c += 1
                    while (c < d) and (nums[d] == nums[d+1]):
                        d -= 1
                    # print(f"a {a} b {b} c {c} d {d} "
                    #       f"lst {lst}")
                    # time.sleep(1)
                    
                elif sum(lst) < target:
                    c += 1
                    while (c < d) and (nums[c] == nums[c-1]):
                        c += 1
                    
                elif sum(lst) > target:
                    d -= 1
                    while (c < d) and (nums[d] == nums[d+1]):
                        d -= 1
                
    return res
                
    

if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    nums = [-3,-2,-1,0,0,1,2,3]
    nums = [0, 0, 0, 0]
    nums = [-1,0,1,2,-1,-4]
    target = -1
    fourSum(nums, target)
