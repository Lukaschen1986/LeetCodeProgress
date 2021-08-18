# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:30:24 2021

@author: ASUS

本题精髓：words建一个哈希表，滑动窗口滚动建哈希表，比较是否相同
"""
from collections import (Counter, defaultdict)


def findSubstring(s, words):
    res = []
    n = len(words[0])*len(words)
    m = len(words[0])
    dct = Counter(words)
    
    for i in range(0, len(s)-n+1):
        x = s[i: i+n]
        dct_compare = defaultdict(int)
        for j in range(0, len(x), m):
            y = x[j: j+m]
            dct_compare[y] += 1
            
            if dct_compare == dct:
                res.append(i)
    
    return res



if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo","bar"]
        
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    
    findSubstring(s, words)
