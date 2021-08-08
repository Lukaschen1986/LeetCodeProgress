# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 12:18:06 2021

@author: ASUS
"""
from collections import Counter

def leastInterval(tasks, n):
    """
    1、计算每个任务出现的次数 counter
    2、找出出现次数最多的任务 x
    3、计算至少需要的时间 (x - 1) * (n + 1)
    4、计算出现次数为 x 的任务总数 k
    5、长度特殊处理
    """
    counter = Counter(tasks)
    x = max(v for (k,v) in counter.items())
    k = sum(1 for (k,v) in counter.items() if v == x)
    res = (x - 1)*(n + 1) + k
    res = max(res, len(tasks))
    return res


if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"]
    n = 2
    leastInterval(tasks, n)
