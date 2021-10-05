# -*- coding: utf-8 -*-

def checkInclusion(s1: str, s2: str) -> bool:
    n = len(s2)
    m = len(s1)
    for i in range(n-m+1):
        tmp = s2[i:i+m]
        if sorted(tmp) == sorted(s1):
            return True

    return False



if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    res = checkInclusion(s1, s2)
    print(res)
