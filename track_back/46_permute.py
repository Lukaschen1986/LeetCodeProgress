# -*- coding: utf-8 -*-
def permute(nums: list) -> list:
    res = []
    
    def track_back(combination, nums):
        if not nums:
            res.append(combination)
        else:
            for i in range(len(nums)):
                track_back(combination + [nums[i]], nums[0:i] + nums[i+1:])
    
    track_back([], nums)
    return res
    
    
if __name__ == "__main__":
    nums = [1, 2, 3]
    permute(nums)
