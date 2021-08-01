# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:59:49 2021

@author: ASUS
"""
from collections import (Counter, defaultdict)

def topKFrequent(nums, k):
    count = Counter(nums)
    lst = count.most_common(k)
    res = []    
    
    for pair in lst:
        res.append(pair[0])
    
    return res


def topKFrequent(nums, k):
    dct = defaultdict(int)
    for x in nums:
        dct[x] += 1
    
    lst = [(k,v) for (k,v) in dct.items()]
    lst.sort(key=lambda x: x[1], reverse=True)
    lst = lst[0:k]
    res = []
    
    for pair in lst:
        res.append(pair[0])
    
    return res
    

if __name__ == "__main__":
    nums = [3,4,4,2,2,4]
    k = 2
