# -*- coding: utf-8 -*-
def wiggleSort(nums):
    nums.sort(reverse=True)  # slzb
    n = len(nums)
    mid = n // 2
    nums[::2], nums[1::2] = nums[mid:], nums[:mid]  # slzb
    return nums


if __name__ == "__main__":
    # nums = [1, 5, 1, 1, 6, 4]
    # nums = [1, 3, 2, 2, 3, 1]
    # nums = [1, 3, 4]
    nums = [1, 1, 2, 1, 2, 2, 1]
    res = wiggleSort(nums)
    print(res)
