# -*- coding: utf-8 -*-
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)

        nums_1 = nums[:]
        nums_1[-1] = 0
        
        dp_1 = [0]*len(nums_1)
        dp_1[0] = nums_1[0]
        for i in range(1, len(nums_1)):
            dp_1[i] = max(dp_1[i-1], nums_1[i]+dp_1[i-2])
        
        nums_2 = nums[:]
        nums_2[0] = 0
        
        dp_2 = [0]*len(nums_2)
        for i in range(1, len(nums_2)):
            dp_2[i] = max(dp_2[i-1], nums_2[i]+dp_2[i-2])
        
        return max(dp_1[-1], dp_2[-1])
