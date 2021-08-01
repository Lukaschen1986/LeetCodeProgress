# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 16:05:57 2021

@author: ASUS
"""
import bisect

def minMeetingRooms(intervals: list) -> int:
    """
    ​O(NlogN) time | O(N) space
    """
    if not intervals:
        return 0
    
    intervals.sort()
    heap = [intervals[0][1]]
    res = 1
    
    for time in intervals[1:]:
        min_time = min(heap)
        if time[0] < min_time:
            res += 1
            bisect.insort(heap, time[1])
        else:
            heap.pop(0)
            bisect.insort(heap, time[1])

    return res
    
    
if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    intervals = [[0,30],[5,10],[15,20],[4,7],[8,12],[30,40]]
    intervals = [[7,10],[2,4]]
    minMeetingRooms(intervals)
