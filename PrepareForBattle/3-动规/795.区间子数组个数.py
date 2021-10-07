# -*- coding: utf-8 -*-


def numSubarrayBoundedMax(nums, left, right):
    n = len(nums)
    dp_1 = dp_2 = 0
    res = 0

    for i in range(n):
        if nums[i] < left:
            dp_1 += 1  # 神来之笔
        elif nums[i] > right:
            dp_1 = 0  # 神来之笔
            dp_2 = 0  # 神来之笔
        else:
            dp_2 = dp_1 + dp_2 + 1  # 神来之笔
            dp_1 = 0  # 神来之笔

        res += dp_2

    return res



if __name__ == "__main__":
    nums = [1, 5, 1, 1, 2, 1, 1, 4, 3]
    nums = [2, 1, 5, 2]
    left = 2
    right = 3
    res = numSubarrayBoundedMax(nums, left, right)
    print(res)
