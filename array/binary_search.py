# -*- coding: utf-8 -*-
def binary_search(lst, target):
    if not lst:
        return False
    
    lst.sort()
    if (target < lst[0]) or (target > lst[-1]):
        return False
    
    L = 0
    R = len(lst) - 1
    while L < R:
        M = (L + R) // 2
        val = lst[M]
        if target == val:
            return True
        elif target < val:
            R = M - 1
        else:
            L = M + 1
        
    return False


if __name__ == "__main__":
    lst = [33, 61, 73, 1, 45, 72, 21, 67, 55]
    lst = []
    target = 33
    binary_search(lst, target)
