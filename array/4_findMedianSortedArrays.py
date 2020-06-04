# -*- coding: utf-8 -*-
def findMedianSortedArrays(nums1: list, nums2: list) -> float:
    nums1.extend(nums2)
    nums1.sort()
    mid = len(nums1) // 2
    
    if len(nums1) % 2 == 0:
        return float((nums1[mid-1] + nums1[mid]) / 2)
    else:
        return float(nums1[mid])
    

if __name__ == "__main__":
    nums1 = [1, 2, 8]
    nums2 = [3, 4]
    findMedianSortedArrays(nums1, nums2)
