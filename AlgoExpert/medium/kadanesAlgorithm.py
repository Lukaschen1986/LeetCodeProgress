# -*- coding: utf-8 -*-
def kadanes_algorithm(nums):
    """
    53. 最大子序和
    # O(n) time | O(N) space
    """
    dp = [0]*len(nums)
    dp[0] = nums[0]
    
    for i in range(1, len(dp)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    
    return max(dp)


def kadanes_algorithm(nums):
    """
    53. 最大子序和
    # O(n) time | O(1) space
    """
    dp = nums[0]
    dp_res = nums[0]
    
    for num in nums[1:]:
        dp = max(dp + num, num)
        dp_res = max(dp_res, dp)

    return dp_res

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10]
    kadanes_algorithm(nums)
