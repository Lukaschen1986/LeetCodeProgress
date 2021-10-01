# -*- coding: utf-8 -*-

def minSubArrayLen(target, nums):
    n = len(nums)
    i = j = 0
    res = float("inf")

    while (j < n) and (i <= j):
        tmp = nums[i:j+1]
        _sum = sum(tmp)
        if _sum < target:
            j += 1
        else:
            res = min(res, len(tmp))
            print(tmp)
            i += 1

    return res if res != float("inf") else 0


if __name__ == "__main__":
    # target = 7; nums = [2, 3, 1, 2, 4, 3]
    # target = 4; nums = [1, 4, 4]
    target = 11; nums = [1, 1, 1, 1, 1, 1, 1, 1]

    res = minSubArrayLen(target, nums)
    print(res)
