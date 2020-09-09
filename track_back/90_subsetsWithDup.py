# -*- coding: utf-8 -*-
def subsetsWithDup(nums: list) -> list:
    res = []
    nums.sort()
    
    def track_back(combination, idx):
        if idx == len(nums):
            if sorted(combination) not in res:
                res.append(combination)
        else:
            track_back(combination + [nums[idx]], idx+1)
            track_back(combination, idx+1)
    
    track_back([], 0)
    return res

    
if __name__ == "__main__":
    nums = [1,2,2]
    subsetsWithDup(nums)
