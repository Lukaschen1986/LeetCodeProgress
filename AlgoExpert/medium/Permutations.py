# -*- coding: utf-8 -*-
def permute(nums):
    """
    全排列
    O(N*N!) time | O(N*N!) space
    """
    res = []
    
    def helper(combination, nums):
        if not nums:
            res.append(combination)
            return 
        else:
            for i in range(len(nums)):
                helper(combination + [nums[i]], nums[0:i] + nums[i+1:])
    
    helper([], nums)
    return res


from itertools import permutations

def permute(nums):
    res = []

    for tpl in permutations(nums):
        lst = list(tpl)
        res.append(lst)
    
    return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    permute(nums)
