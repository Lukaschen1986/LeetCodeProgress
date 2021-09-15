# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:30:24 2021

@author: ASUS
"""

def findSubstring(s, words):
    """
    time = O(N)
    space = O(N)
    """
    words.sort()
    n = len(words)
    m = len(words[0])
    length = m*n
    res = []
    
    for i in range(0, len(s)-length+1):
        j = i + length
        tmp = s[i:j]
        lst = []
        for k in range(0, len(tmp), m):
            x = tmp[k:k+m]
            lst.append(x)
        if sorted(lst) == words:
            res.append(i)
    
    return res
    


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo","bar"]
        
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
