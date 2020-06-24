# -*- coding: utf-8 -*-
def search(nums: list, target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        return -1
