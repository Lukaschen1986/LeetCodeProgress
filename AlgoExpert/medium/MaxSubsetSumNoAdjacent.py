# -*- coding: utf-8 -*-
def max_subset_sum_no_adjacent(nums: list) -> int:
    """
    不相邻元素的最大和
    ​# O(N) time | O(N) space
    """
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    return dp[-1]
    

def max_subset_sum_no_adjacent(nums: list) -> int:
    """
    不相邻元素的最大和
    ​# O(N) time | O(1) space
    """
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        far_max = nums[0]
        pre_max = max(far_max, nums[1])
        
        for num in nums[2:]:
            curr_max = max(pre_max, num + far_max)
            pre_max, far_max = curr_max, pre_max
            
    return curr_max

    
if __name__ == "__main__":
    nums = [7, 10, 12, 7, 9, 14]
    max_subset_sum_no_adjacent(nums)
