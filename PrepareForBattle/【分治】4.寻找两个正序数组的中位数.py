# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 15:31:44 2021

@author: ASUS

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
"""
def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    
    if len(nums) % 2 == 0:
        mid_r = len(nums) // 2
        mid_l = mid_r - 1
        return (nums[mid_l] + nums[mid_r]) / 2
    else:
        mid = len(nums) // 2
        return nums[mid]
    
    
if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    findMedianSortedArrays(nums1, nums2)
