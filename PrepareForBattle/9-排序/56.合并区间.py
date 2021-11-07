# -*- coding: utf-8 -*-
def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    
    for pair in intervals[1:]:
        start, end = pair[0], pair[1]
        if start <= res[-1][1]:
            prev = res.pop()
            prev[1] = max(prev[1], end)
            res.append(prev)
        else:
            res.append(pair)
    
    return res
    
    
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    # [[1,6],[8,10],[15,18]]
    merge(intervals)
    
