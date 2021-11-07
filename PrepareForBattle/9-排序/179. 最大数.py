# -*- coding: utf-8 -*-
def largestNumber(nums):
    nums = [str(x) for x in nums]
    nums.sort(key=lambda x: x[0], reverse=True)
    n = len(nums)
    res = "0"
    
    while True:
        for i in range(n-1):
            j = i + 1
            tmp_1 = nums[i] + nums[j]
            tmp_2 = nums[j] + nums[i]
            if tmp_1 > tmp_2:
                continue
            else:
                nums[i], nums[j] = nums[j], nums[i]
        
        s = "".join(nums)
        if int(s) > int(res):
            res = s
        else:
            break
    
    return res
    
    
    
if __name__ == "__main__":
    nums = [3,30,34,5,9]
    nums = [10,2]
    nums = [0, 0, 0]
