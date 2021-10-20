#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import defaultdict

def killProcess(pid, ppid, kill):
    dct = defaultdict(list)
    res = [kill]
    stack = [kill]

    for (k, v) in zip(ppid, pid):
        dct[k].append(v)
    dct.pop(0)
    print(dct)
    while stack:
        node = stack.pop()
        lst = dct.get(node)
        if not lst:
            continue
        res.extend(lst)
        stack.extend(lst)

    return res


if __name__ == "__main__":
    pid = [1, 3, 10, 5, 3, 4]
    ppid = [3, 0, 5, 3, 2, 2]
    kill = 3
    res = killProcess(pid, ppid, kill)
    print(res)
