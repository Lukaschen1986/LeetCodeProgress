# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:13:23 2021

@author: ASUS
"""
from collections import defaultdict

def shortestDistanceIII(words, word1, word2):
    """
    word1 和 word2 是有可能相同的。
    time = O(N^2)
    space = O(1)
    """
    dct = defaultdict(list)
    for (i,w) in enumerate(words):
        dct[w].append(i)
    
    idx1 = dct.get(word1)
    idx2 = dct.get(word2)
    dist = float("inf")
    
    for i in idx1:
        for j in idx2:
            if i == j:
                continue
            else:
                dist = min(dist, abs(i-j))
    
    return dist


if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "makes"
