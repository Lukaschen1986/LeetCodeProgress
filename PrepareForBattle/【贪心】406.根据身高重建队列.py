# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:39:50 2021

@author: ASUS
"""

def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    res = [people[0]]
    
    for i in range(1, len(people)):
        val, compare = people[i]
        idx = 0
        j = 0
        
        while (idx < compare) and (j < len(res)):
            if res[j][0] >= val:
                idx += 1
            j += 1
        
        res.insert(idx, people[i])
    
    return res
        
    
if __name__ == "__main__":
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    reconstructQueue(people)
