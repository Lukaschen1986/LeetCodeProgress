# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 19:59:37 2021

@author: ASUS
"""


def findPeakElement(nums) -> int:
    """
    time = O(logN)
    space = O(1)
    """
    n = len(nums)

    # 特例
    if n < 4:
        return nums.index(max(nums))
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return n-1

    # 普通
    i = 1
    j = n-2
    while i <= j:
        if (nums[i] > nums[i-1]) and (nums[i] > nums[i+1]):
            return i
        elif (nums[j] > nums[j-1]) and (nums[j] > nums[j+1]):
            return j
        else:
            i += 1
            j -= 1


if __name__ == "__main__":
    nums = [1,2,1,3,5,6,4]
