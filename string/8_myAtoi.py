# -*- coding: utf-8 -*-
import re

def myAtoi(s: str) -> int:
    re_complie = re.compile(r"^[\+\-]?[\d]+")
    str_ = s.lstrip()
    num = int(*re_complie.findall(str_))
    
    if num < -2**31:
        return -2**31
    elif num > 2**31 - 1:
        return 2**31 - 1
    else:
        return num


if __name__ == "__main__":
    s = "   -42"
    s = "words and 987"
    myAtoi(s)
