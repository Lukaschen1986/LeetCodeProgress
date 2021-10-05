# -*- coding: utf-8 -*-


def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    res = []

    for a in range(0, n-3):
        for b in range(a+1, n-2):
            c = b + 1
            d = n - 1
            while c < d:
                _sum = nums[a] + nums[b] + nums[c] + nums[d]
                lst = [nums[a], nums[b], nums[c], nums[d]]
                if _sum == target:
                    if sorted(lst) not in res:
                        res.append(lst)
                    c += 1
                    d -= 1
                elif _sum < target:
                    c += 1
                elif _sum > target:
                    d -= 1

    return res


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    res = fourSum(nums, target)
    print(res)
