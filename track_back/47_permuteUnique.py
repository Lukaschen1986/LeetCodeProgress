# -*- coding: utf-8 -*-
def permuteUnique(nums: list) -> list:
    res = []
    
    def track_back(combination, nums):
        if (not nums) and (combination not in res):
            res.append(combination)
        else:
            for i in range(len(nums)):
                track_back(combination + [nums[i]], nums[0:i] + nums[i+1:])
    
    track_back([], nums)
    return res
    

if __name__ == "__main__":
    nums = [1, 1, 2]
    permuteUnique(nums)
