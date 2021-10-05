# -*- coding: utf-8 -*-

def threeSumSmaller(nums, target):
    n = len(nums)
    nums.sort()
    res = 0

    for k in range(n-2):
        i = k + 1
        j = n - 1
        while i < j:
            _sum = nums[k] + nums[i] + nums[j]
            if _sum >= target:
                j -= 1
            else:
                res += j - i  # 神来之笔
                i += 1

    return res



if __name__ == "__main__":
    nums = [-3, 0, 1, 3, 4]
    target = 2

    # nums = [-2, 0, 1, 3]
    # target = 2
    #
    # nums = [-2, 0, 1, 0, 2, 3]
    # target = 2

    res = threeSumSmaller(nums, target)
    print(res)
