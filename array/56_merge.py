# -*- coding: utf-8 -*-
def merge(intervals: list) -> list:
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0], reverse=False)
    res = [intervals[0]]
    
    for pair in intervals[1:]:
        if pair[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], pair[1])
        else:
            res.append(pair)
    
    return res
        
    
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[4,5]]
    intervals = []
    intervals = [[1,4],[0,4]]
    intervals = [[1, 4], [2, 3]]
    res = merge(intervals)
    print(res)
