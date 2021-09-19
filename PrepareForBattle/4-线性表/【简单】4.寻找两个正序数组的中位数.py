# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:48:30 2021

@author: ASUS
"""

def findMedianSortedArrays(nums1, nums2) -> float:
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)
    mid = n // 2

    if n % 2 == 0:
        # 偶数
        return (nums[mid-1] + nums[mid])/2
    else:
        # 奇数
        return nums[mid]
