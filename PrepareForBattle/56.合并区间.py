# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 17:28:36 2021

@author: ASUS
"""
def merge(intervals: list) -> list:
    """
    ​O(NlogN) time | O(N) space
    """
    intervals.sort()
    res = [intervals[0]]

    for pair in intervals[1:]:
        k = res[-1][1]
        a = pair[0]
        b = pair[1]
        if a > k:
            res.append(pair)
        elif a <= k < b:
            previous = res.pop()
            previous[1] = b
            res.append(previous)
        elif b <= k:
            continue

    return res
