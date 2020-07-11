# -*- coding: utf-8 -*-
def strStr(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    else:
        return haystack.index(needle)
    
    
if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    strStr(haystack, needle)
