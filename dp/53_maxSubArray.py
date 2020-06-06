# -*- coding: utf-8 -*-
def maxSubArray(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    
    dp = [0]*len(nums)
    dp[0] = nums[0]
    
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    
    return max(dp)


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    maxSubArray(nums)
