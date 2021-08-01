# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:03:32 2021

@author: ASUS

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
"""
def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    
    for pair in intervals[1:]:
        last = res[-1][1]
        start = pair[0]
        end = pair[1]
        if start > last:
            res.append(pair)
        else:
            prev = res.pop()
            prev[1] = max(prev[1], end)
            res.append(prev)
    
    return res
    
    
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # [[1,6],[8,10],[15,18]]
    merge(intervals)
    
