# -*- coding: utf-8 -*-
def firstMissingPositive(nums: list) -> int:
    if 1 not in nums:
        return 1
    else:
        nums = sorted(x for x in nums if x >= 1)
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                return nums[i-1] + 1
        
        return nums[-1] + 1


if __name__ == "__main__":
    nums = [3, 4, -1, 1]
    nums = [0, 1, 2, 7, 8, 10, 12]
