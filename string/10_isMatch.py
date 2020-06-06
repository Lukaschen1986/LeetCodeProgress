# -*- coding: utf-8 -*-
import re

def isMatch(s: str, p: str) -> bool:
    re_compile = re.compile(p)
    lst = re_compile.findall(s)
    
    if s in lst:
        return True
    else:
        return False
    

if __name__ == "__main__":
    s = "aa"
    p = "a*"
    isMatch(s, p)
