# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:29:37 2021

@author: ASUS
"""

def calculateTime(keyboard, word):
    """
    time = O(N)
    space = O(1)
    """
    i = 0
    res = 0

    for w in word:
        j = keyboard.index(w)
        time = abs(i - j)
        res += time
        i = j
    
    return res


if __name__ == "__main__":
    keyboard = "pqrstuvwxyzabcdefghijklmno"
    word = "leetcode"
