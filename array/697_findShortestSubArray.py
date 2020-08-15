# -*- coding: utf-8 -*-
def findShortestSubArray(nums: list) -> int:
    dct = {}
    for x in nums:
        if x not in dct:
            dct[x] = 1
        else:
            dct[x] += 1
    
    minlen = float("inf")
    lst = [k for (k,v) in dct.items() if v == max(dct.values())]
    for x in lst:
        a = nums.index(x)
        b = len(nums) - nums[::-1].index(x)
        minlen = min(minlen, len(nums[a:b]))
    
    return minlen
        


if __name__ == "__main__":
    nums = [1,2,2,3,1,4,2,1]
    nums = []
    nums = [1,2]
    findShortestSubArray(nums)
