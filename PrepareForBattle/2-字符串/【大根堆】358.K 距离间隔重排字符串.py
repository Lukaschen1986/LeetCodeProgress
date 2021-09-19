# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:59:09 2021

@author: ASUS
"""

from collections import Counter
import heapq


def rearrangeString(s: str, k: int) -> str:
    """
    time = O(logN)
    space = O(N)
    """
    if k <= 1:
        return s
    n = len(s)
    count = Counter(s)
    priority_queue = [(-v,k) for (k,v) in count.items()] # 神来之笔，大根堆
    heapq.heapify(priority_queue) # 建堆
    res = ""
    
    while priority_queue:
        lst = [] # 神来之笔
        
        for i in range(k):
            if not priority_queue: # 神来之笔
                if len(res) == n:
                    return res
                else:
                    return ""
            num, w = heapq.heappop(priority_queue)
            num += 1
            res += w
            if num != 0: # 神来之笔
                lst.append((num, w))
        
        for pair in lst: # 神来之笔
            heapq.heappush(priority_queue, pair)
    
    return res


if __name__ == "__main__":
    s = "ccaabb"
    k = 1

    # s = "aaadbbcc"
    # k = 2
    res = rearrangeString(s, k)
    print(res)
