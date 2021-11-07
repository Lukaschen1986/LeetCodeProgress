# -*- coding: utf-8 -*-
import heapq


def findLongestWord(s, dictionary):
    heap = []
    n = len(s)

    for w in dictionary:
        length = helper(w, n)
        if length == len(w):
            heapq.heappush(heap, (-length, w))

    print(heap)
    if not heap:
        return ""
    else:
        length, w = heapq.heappop(heap)
        return w

def helper(w, n):
    m = len(w)
    length = 0
    i = 0
    j = 0
    while (i < n) and (j < m):
        if w[j] == s[i]:
            length += 1
            i += 1
            j += 1
        else:
            i += 1

    return length


if __name__ == "__main__":
    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]

    s = "abpcplea"
    dictionary = ["a", "b", "c"]
    res = findLongestWord(s, dictionary)
    print(res)
