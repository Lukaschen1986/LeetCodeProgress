# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:58:20 2021

@author: ASUS
"""
def three_number_sum(array: list, target: int) -> list:
    """
    ​O(N^2) time | O(N) space
    """
    res = []
    array.sort()
    
    for k in range(0, len(array)-2):
        i = k + 1
        j = len(array) - 1
        
        while i < j:
            three_sum = array[k] + array[i] + array[j]
            if three_sum == target:
                res.append([array[k], array[i], array[j]])
                i += 1
                j -= 1
            elif three_sum < target:
                i += 1
            elif three_sum > target:
                j -= 1
    
    return res


if __name__ == "__main__":
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0
    three_number_sum(array, target)
    
