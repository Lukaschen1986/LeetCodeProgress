# -*- coding: utf-8 -*-
def find132pattern(nums) -> bool:
    # 特例
    n = len(nums)
    if n <= 2:
        return False

    # 常规
    stack = []
    k = None

    for i in range(n-1, -1, -1):
        if k and (nums[i] < nums[k]):  # 神来之笔
            return True

        while stack and (nums[i] > nums[stack[-1]]):  # 单调递减栈
            k = stack.pop()

        stack.append(i)

    return False


if __name__ == "__main__":
    nums = [-1, 3, 2, 0]
    res = find132pattern(nums)
    print(res)
