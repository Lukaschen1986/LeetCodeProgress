# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 15:22:17 2021

@author: ASUS
"""
def canAttendMeetings(intervals: list) -> bool:
    """
    ​O(NlogN) time | O(1) space
    """
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
        
    return True


if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    intervals = [[7,10],[2,4]]
    canAttendMeetings(intervals)
